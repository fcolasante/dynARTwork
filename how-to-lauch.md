# How to launch
1. Connect ESP32 and Grid Eye
2. Lauch mosquitto rsmb
3. Lanch gateway_riot.py

This 3 step enable device data (push data from Grid Eye to Google IoT Core)

Now, we need to setup our Raspberry Pi (that fetch processed artworks)
which is conprocessed-subnected to Monitor through HDMI output.
4. Lauch Raspberry (connect HDMI using miniHDMI-HDMI adapter)
5. Lauch `devices/stm32/rasp_polling.py`


# How to setup
1. Flash ESP32
2. Flash Raspbian OS (micro SD)
3. Access with SSH
4. SCP files
5. Setup Coud part (PubSub, IoTCore,...)
