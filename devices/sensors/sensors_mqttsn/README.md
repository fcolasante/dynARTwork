## How to setup a RIOT device 
This application demonstrates the usage of the emCute (MQTT-SN) module in RIOT.


## Setup
For using this example, two prerequisites have to be fullfilled:

1. You need a running MQTT broker that supports MQTT-SN or a running MQTT-SN
   gateway that is connected to a running MQTT broker
2. Your RIOT node needs to be able to speak to that broker/gateway


### Setting up a broker

1. Start the broker:
```s
./broker_mqtts config.conf
```

You can refer to
https://rawgit.com/MichalFoksa/rsmb/master/rsmb/doc/gettingstarted.htm for more
configuration options.

2. run `ifconfig` and check the `IPv6` address of the broker. `<IPv6_broker>`

## Flash and run

Install ESP32 Toolkit and then:

```s
export PATH=$PATH:$HOME/university/esp/xtensa-esp32-elf/bin
export ESP32_SDK_DIR=$HOME/university/esp/esp-idf
make flash BOARD=esp32-wroom-32 term
```

## Usage
This example maps all available MQTT-SN functions to shell commands. Simply type
`help` to see the available commands. The most important steps are explained
below:

- To connect to a broker, use the `con` command:

```s
con <IPv6_broker> 1885
set_device <dynartwork_name>
pub_telemetry
```

