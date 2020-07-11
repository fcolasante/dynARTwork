# Google Cloud Platform

In Google Cloud Platform we use different modules:
- Google IoT Core
- Google Pub-Sub
- Google Bucket (what is the real name?)
- Cloud Run



## Google Pub-Sub

We have 2 different topics:
- `sensors-topic`: Type of delivery: **Push**.
This topic has an **Endpoint push**: `https://sensors-service-ejdw7fcwpq-ew.a.run.app`.
(I think that is the endpoint of Google Compute Engine where runs the Docker instance of Flusk).


- `processed-topic`: type of delivery: **Pull**. 


## Cloud Run
We have a single instance of Cloud run called `sensors-service`.
It is a Docker container which runs a **Flask** application with **Gunicorn**, a Python WSGI HTTP Server for UNIX.

We have a single API which is : `POST` on `/`.
It receive a PubSub message where is wrapped the IoT telemetry and manipulate this raw telemetry data
using `MatPlotlib` and Wand.
It computes sequentially this 2 step.
1. Create an heatmap from Raw telemetry data using `Matplotlib`.
2. Fetch the original image uploaded by the artists, (correlated to the telemetry) and merge
this due picture in a new image and upload it on a second bucket (`processed-images`???).
  

## Flow
1. IoT devices that runs on RIOT-OS and send messages over the MQTT-SN protocol.
2. Mosquitto RSMB broker which convert the MQTT-SN packet into MQTT.
3. Custom transparent gateway which use Paho MQTT library connected to Mosquitto RSMB broker
which is directly connected to *Google IoT Core* and send messages on GCP.
4. Google IoT core is configured with a single **Register**: (Pub-sub topic on telemetry data):
`projects/dynartwork-277815/topics/sensors-topic`.
5. The Pub-Sub `sensors-topic` have a single subscription of type Push on ``https://sensors-service-ejdw7fcwpq-ew.a.run.app`
which call the Cloud Run instance.
6. The cloud Run (Flask) convert raw data in picture and merge it with the original picture and upload
the new image on a Bucket.
7. It is setted an automatic notification on a PubSub topic `processed-topic` where
is sent the messages of `Google Bucket`.
8. A Python Script on the Raspberry PI (pull type) check the `processed-topic`, download the new image 
when it is arrive and show it on the HDMI monitor.


I will notice that everything is asynch. The flow is trigger on cascade of events.


