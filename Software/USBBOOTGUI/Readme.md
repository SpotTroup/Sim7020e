USB BOOT GUI 

The Raspberry Pi Zero and Pi Zero W feature a USB OTG port, allowing users to configure the device as (amongst other things) an Ethernet device. In this mode, it is possible to control the Pi Zero’s GPIO pins over USB from another computer using the remote GPIO feature.

6.1. GPIO expander method - no SD card required
The GPIO expander method allows you to boot the Pi Zero over USB from the PC, without an SD card. Your PC sends the required boot firmware to the Pi over the USB cable, launching a mini version of Raspbian and booting it in RAM. The OS then starts the pigpio daemon, allowing “remote” access over the USB cable.
