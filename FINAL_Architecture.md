# Architecture
Infrastructure that collects data from sensors/Internet, processes it using Machine Learning and shows the output using video/sound/smell.

![](assets/final_architecture.png)



Our architecture is composed by 4 main parts:
1. **Sensors** (IoT element) : It is the input of our DynARTwork algorithm. We use an IoT device performing RIOT-OS to collect informations in the Museum using a  [Panasonic Grid Eye sensor](https://industrial.panasonic.com/ww/products/sensors/built-in-sensors/grid-eye).

![](assets/2020_0710_160314.png)

1. **Cloud components**: We will use the Google Cloud Platform *(IoT Core, Firestore, Hosting, Pub/Sub, Cloud Vision API and Storage)* to collect and manipulate data.
2. **Artists' WebApp** (End-user components): This part will be used by the artists. It will have a simple UI/UX interface to hide all tech detail in order to permit artists to build their DyArtwork without worrying about technical details.
  We use Angular + [Material](https://material.angular.io/) + Firebase to create easily a [PWA](https://web.dev/progressive-web-apps/). It will be responsive and it will be immediately ready for Android / iOS and on the web.
3. **Actuators** (IoT elements): We will create an IoT device *(Raspberry PI 0)* which pull DynArtwork from the Cloud and it will redirect this stream to the HDMI output where the museum projector will be connected.

## Sensors:
ESP32 + I2C  + GRID EYE, CONNECTION WIRES, ETC... + DATASHEET + MAXIM ONE-WIRE

PORTS + CODE



## Actuators:
Raspberry Pi 0 W which is connected through mini-HDMI to Projector



#### Google IoT Core

#### Google Pub-Sub

#### Google Cloud Vision

#### Google Storage

#### ESP32

#### Grid Eye

#### Raspberry Pi 0 W

