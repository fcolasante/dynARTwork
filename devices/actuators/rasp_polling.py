import os
import argparse
import json
import time
#import cv2
from wand.image import Image
from google.cloud import storage
from google.cloud import pubsub_v1
import subprocess
from google.auth import jwt
import time

image = None

def poll_notifications(project, subscription_name):
    """Polls a Cloud Pub/Sub subscription for new GCS events for display."""
    # [BEGIN poll_notifications]

    service_account_info = json.load(open("service_account.json"))
    audience = "https://pubsub.googleapis.com/google.pubsub.v1.Subscriber"

    credentials = jwt.Credentials.from_service_account_info(
        service_account_info, audience=audience
    )
    subscriber = pubsub_v1.SubscriberClient(credentials=credentials)

    subscription_path = subscriber.subscription_path(
        project, subscription_name
    )

    def download_image(name, bucketName="dynartwork-277815.appspot.com"):
        storage_client = storage.Client.from_service_account_json('service_account.json')
        bucket = storage_client.get_bucket(bucketName)
        # get bucket data as blob
        print(f'Opening {bucketName}/{name}')
        blob = bucket.get_blob(name)
        json_data = blob.download_as_string()
        text_file = open(name, "wb")
        n = text_file.write(json_data)
        text_file.close()

    def callback(message):
        #show_image(message.attributes['objectId'])
        #print("Received message:\n{}".format(summarize(message)))
        data = message.data.decode("utf-8")
        attributes = message.attributes

        event_type = attributes["eventType"]
        bucket_id = attributes["bucketId"]
        object_id = attributes["objectId"]
        print(object_id)
        message.ack()
        var = "Message not important"
        if "data" in object_id:
            originalName= object_id[5:-4]
            imageName = f'{originalName}_showed.jpg'
            download_image(imageName, 'processed_artworks')
            # display the image
            print("Showing image:{}".format(imageName))
            global image
            previousImage = image
            image = subprocess.Popen(["feh", "--hide-pointer", "-x", "-q", "-B", "black", f"/home/pi/Documents/{imageName}"])
            time.sleep(2)
            previousImage.kill()
            var = "Image correctly showed"
        print("Result of callback:{}".format(var))
        

    subscriber.subscribe(subscription_path, callback=callback)
    # The subscriber is non-blocking, so we must keep the main thread from
    # exiting to allow it to process messages in the background.
    print("Listening for messages on {}".format(subscription_path))
    global image
    image = subprocess.Popen(["feh", "--hide-pointer", "-x", "-F", f"/home/pi/Documents/dynartwork.png"])
    while True:
        time.sleep(60)
    # [END poll_notifications]


if __name__ == "__main__":
    poll_notifications("dynartwork-277815", "processed-sub")
