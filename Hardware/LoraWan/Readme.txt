LoraWan:

That mobile network operators adopt their technology for IoT deployments over both city and nationwide low power, wide-area networks (LPWANs).
radio frequency bands as the 169 MHz, 433 MHz, 868 MHz for Europe

-LoRa: the physical layer,
-LoRaWAN (Long Range Wide Area Network): the upper layers.


Heltec Lora 32  Microprocessor: ESP32 (dual-core 32-bit MCU + ULP core), with LoRa node chip SX1276/SX1278;
-> https://heltec.org/project/wifi-lora-32/


Libraries:
uPyLora -> https://github.com/Wei1234c/SX127x_driver_for_MicroPython_on_ESP8266

Test-Reqeirements :
Ping-pong: sends ping-pong messages between the nodes (bidirectional communication)
Sender or receiver: unidirectional communication between the nodes.


Lets start:
1.Install Micropython to the ESP32: 
Firmware: https://micropython.org/download/esp32/
Tutorial: https://lemariva.com/blog/2017/10/micropython-getting-started

Useable IDEs: VSC or Atom.iO  ( with Platfrom IO Add-on/Plug-In)
$ apt-get install clang  TLTR -> https://docs.platformio.org/en/latest/integration/ide/atom.html#ii-clang-for-intelligent-code-completion
install Atom.io 
menu->preferences->install-> install Platform IO

VSC: ( Platform IO has more support then only C in VSC !!!)
Open VSCode Extension Manager
Search for official PlatformIO IDE extension
Install PlatformIO IDE TLTR -> https://docs.platformio.org/en/latest/
install Platform : ESP32 https://community.platformio.org/t/esp32-dev-difference-between-framework-espidf-framework-arduino-and-framework-arduino-espidf/10560
