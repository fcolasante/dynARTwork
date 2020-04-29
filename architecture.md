# Architecture
Infrastructure that collects data from sensors/Internet, processes it using Machine Learning and shows the output using video/sound/smell.

![](assets/architecture.svg)


providing details on the technical aspects of the product/service, including a high-level presentation of the conceptual architecture of the software and hardware components that make up the product/service, a description of the main software/hardware components (e.g., 1 paragraph for each component), how these components interact (e.g., network protocols, APIs used), a network architecture clearly depicting the IoT elements, Edge components, Cloud components, End-user components.

Our architecture is composed by 4 main parts:
1. **Sensors** (IoT elements) : It is the input of our DynArtwork algorithm. We will use IoT-devices to collects informations in the Museum.
2. **Cloud components**: We will use the Cloud to collect our informations: sensors and artist setup to build the DynArtwork.
3. **Artists' webapp** (End-user components): This part will be used by the artists. It will have a simple UI/UX interface to hide all tech detail in order
to permit artists to build their DyArtwork not worrying about technical details.
4. **Actuators** (IoT elemets): We will create an IoT devices which pull DynArtwork from the Cloud (ex. RTMP/RSTP) and it will redirect this stream to the HDMI output where the museum projector will be connected.


## Sensors:
- Thermal camera, temperature, humidity,....
- External data (API), internally but in another places(ex. Rome)
- Simulated data/IoT-Lab

## Actuators:
- Projector/monitor
- Sound
- Smell: [Product](http://www.emhealia.com/em-station/) [History](https://www.linkedin.com/pulse/da-zero-prodotto-francesco-colasante/) 
- Video-Mapping?


## Technology:
- IoT sensors
- External API
- Cloud Machine Learning

