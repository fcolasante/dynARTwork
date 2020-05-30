#import os
#from google.cloud import pubsub_v1
#import json
#from google.auth import jwt
#
#service_account_info = json.load(open("service_account.json"))
#
#
#audience = "https://pubsub.googleapis.com/google.pubsub.v1.Subscriber"
#
#credentials = jwt.Credentials.from_service_account_info(
#    service_account_info, audience=audience
#)
#
#publisher_audience = "https://pubsub.googleapis.com/google.pubsub.v1.Publisher"
#credentials_pub = credentials.with_claims(audience=publisher_audience)
#publisher = pubsub_v1.PublisherClient(credentials=credentials_pub)
#topic_name = 'projects/dynartwork/topics/sensors-topic'
#publisher.create_topic(topic_name)
#publisher.publish(topic_name, b'My first message!', spam='eggs')
#"""Publishes multiple messages to a Pub/Sub topic with an error handler."""
#import time
#
#from google.cloud import pubsub_v1
#
#project_id = "dynartwork-277815"
#topic_name = "sensors-topic"
#
#publisher = pubsub_v1.PublisherClient()
#topic_path = publisher.topic_path(project_id, topic_name)
#
#futures = dict()
#
#def get_callback(f, data):
#    def callback(f):
#        try:
#            print(f.result())
#            futures.pop(data)
#        except:  # noqa
#            print("Please handle {} for {}.".format(f.exception(), data))
#
#    return callback
#
#for i in range(10):
#    data = str(i)
#    futures.update({data: None})
#    # When you publish a message, the client returns a future.
#    future = publisher.publish(
#        topic_path, data=data.encode("utf-8")  # data must be a bytestring.
#    )
#    futures[data] = future
#    # Publish failures shall be handled in the callback function.
#    future.add_done_callback(get_callback(future, data))
#
## Wait for all the publish futures to resolve before exiting.
#while futures:
#    time.sleep(5)
#
#print("Published message with error handler.")





import argparse
import datetime
import json
import os
import ssl
import time
import numpy as np
import jwt
import paho.mqtt.client as mqtt


def create_jwt(project_id, private_key_file, algorithm):
    """Create a JWT (https://jwt.io) to establish an MQTT connection."""
    token = {
        'iat': datetime.datetime.utcnow(),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'aud': project_id
    }
    with open(private_key_file, 'r') as f:
        private_key = f.read()
    print('Creating JWT using {} from private key file {}'.format(
        algorithm, private_key_file))
    return jwt.encode(token, private_key, algorithm=algorithm)


def error_str(rc):
    """Convert a Paho error to a human readable string."""
    return '{}: {}'.format(rc, mqtt.error_string(rc))


class Device(object):
    """Represents the state of a single device."""

    def __init__(self):
        self.temperature = 0
        self.fan_on = False
        self.connected = False

    #def update_sensor_data(self):
    #    """Pretend to read the device's sensor data.
    #    If the fan is on, assume the temperature decreased one degree,
    #    otherwise assume that it increased one degree.
    #    """
    #    if self.fan_on:
    #        self.temperature -= 1
    #    else:
    #        self.temperature += 1

    def wait_for_connection(self, timeout):
        """Wait for the device to become connected."""
        total_time = 0
        while not self.connected and total_time < timeout:
            time.sleep(1)
            total_time += 1

        if not self.connected:
            raise RuntimeError('Could not connect to MQTT bridge.')

    def on_connect(self, unused_client, unused_userdata, unused_flags, rc):
        """Callback for when a device connects."""
        print('Connection Result:', error_str(rc))
        self.connected = True

    def on_disconnect(self, unused_client, unused_userdata, rc):
        """Callback for when a device disconnects."""
        print('Disconnected:', error_str(rc))
        self.connected = False

    def on_publish(self, unused_client, unused_userdata, unused_mid):
        """Callback when the device receives a PUBACK from the MQTT bridge."""
        print('Published message acked.')

    def on_subscribe(self, unused_client, unused_userdata, unused_mid,
                     granted_qos):
        """Callback when the device receives a SUBACK from the MQTT bridge."""
        print('Subscribed: ', granted_qos)
        if granted_qos[0] == 128:
            print('Subscription failed.')

    def on_message(self, unused_client, unused_userdata, message):
        """Callback when the device receives a message on a subscription."""
        payload = message.payload.decode('utf-8')
        print('Received message \'{}\' on topic \'{}\' with Qos {}'.format(
            payload, message.topic, str(message.qos)))

        # The device will receive its latest config when it subscribes to the
        # config topic. If there is no configuration for the device, the device
        # will receive a config with an empty payload.
        if not payload:
            return

        # The config is passed in the payload of the message. In this example,
        # the server sends a serialized JSON string.
        data = json.loads(payload)
        #if data['fan_on'] != self.fan_on:
        #    # If changing the state of the fan, print a message and
        #    # update the internal state.
        #    self.fan_on = data['fan_on']
        #    if self.fan_on:
        #        print('Fan turned on.')
        #    else:
        #        print('Fan turned off.')


def parse_command_line_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Example Google Cloud IoT MQTT device connection code.')
    parser.add_argument(
        '--project_id',
        default=os.environ.get("GOOGLE_CLOUD_PROJECT"),
        required=True,
        help='GCP cloud project name.')
    parser.add_argument(
        '--registry_id', required=True, help='Cloud IoT registry id')
    parser.add_argument(
        '--device_id',
        required=True,
        help='Cloud IoT device id')
    parser.add_argument(
        '--private_key_file', required=True, help='Path to private key file.')
    parser.add_argument(
        '--algorithm',
        choices=('RS256', 'ES256'),
        required=True,
        help='Which encryption algorithm to use to generate the JWT.')
    parser.add_argument(
        '--cloud_region', default='us-central1', help='GCP cloud region')
    parser.add_argument(
        '--ca_certs',
        default='roots.pem',
        help='CA root certificate. Get from https://pki.google.com/roots.pem')
    parser.add_argument(
        '--num_messages',
        type=int,
        default=1,
        help='Number of messages to publish.')
    parser.add_argument(
        '--mqtt_bridge_hostname',
        default='mqtt.googleapis.com',
        help='MQTT bridge hostname.')
    parser.add_argument(
        '--mqtt_bridge_port', type=int, default=8883, help='MQTT bridge port.')
    parser.add_argument(
        '--message_type', choices=('event', 'state'),
        default='event',
        help=('Indicates whether the message to be published is a '
              'telemetry event or a device state message.'))

    return parser.parse_args()


def main():
    args = parse_command_line_args()

    # Create the MQTT client and connect to Cloud IoT.
    client = mqtt.Client(
        client_id='projects/{}/locations/{}/registries/{}/devices/{}'.format(
            args.project_id,
            args.cloud_region,
            args.registry_id,
            args.device_id))
    client.username_pw_set(
        username='unused',
        password=create_jwt(
            args.project_id,
            args.private_key_file,
            args.algorithm))
    client.tls_set(ca_certs=args.ca_certs, tls_version=ssl.PROTOCOL_TLSv1_2)

    device = Device()

    client.on_connect = device.on_connect
    client.on_publish = device.on_publish
    client.on_disconnect = device.on_disconnect
    client.on_subscribe = device.on_subscribe
    client.on_message = device.on_message

    client.connect(args.mqtt_bridge_hostname, args.mqtt_bridge_port)

    client.loop_start()

    # This is the topic that the device will publish telemetry events
    # (temperature data) to.
    mqtt_telemetry_topic = '/devices/{}/events'.format(args.device_id)
    

    # This is the topic that the device will receive configuration updates on.
    mqtt_config_topic = '/devices/{}/config'.format(args.device_id)

    # Wait up to 5 seconds for the device to connect.
    device.wait_for_connection(5)

    # Subscribe to the config topic.
    client.subscribe(mqtt_config_topic, qos=1)

    # Update and publish temperature readings at a rate of one per second.
    for _ in range(args.num_messages):
        # In an actual device, this would read the device's sensors. Here,
        # you update the temperature based on whether the fan is on.
        #device.update_sensor_data()
        array_to_send = np.random.uniform(0, 1, (8,8))
        lists = array_to_send.tolist()
        #dic = {}
        #dic['Matrix'] = array_to_send
        # Report the device's temperature to the server by serializing it
        # as a JSON string.
        payload = json.dumps({'Matrix 8x8': lists})
        print('Publishing payload', payload)
        client.publish(mqtt_telemetry_topic, payload, qos=1)
        # Send events every second.
        time.sleep(1)

    client.disconnect()
    client.loop_stop()
    print('Finished loop successfully. Goodbye!')


if __name__ == '__main__':
    main()
