The raspberry pi zero W has a WiFi module that allows setting up the device headless. To do this, please follow this wiki: http://wiki.lofarolabs.com/index.php/Install_Raspbian
Once the device is setup headless or with monitor, keyboard and mouse, please start off with making sure that everything is updated.
sudo apt-get update
sudo apt-get install upgrade -Y
Once everything is updated and the device is ready, please start validating that UART is enabled.
•	sudo raspi-config
•	option 5 - interfacing options
•	option P6 - serial
•	Would you like a login shell to be accessible over serial? -> No
•	Would you like the serial port hardware to be enabled? -> Yes
 
With UART configured please check whether or not you see the device we will be interfacing with /dev/ttyS0 with command: ls -l /dev | grep tty.
This project utilizes the UART protocol for communicating with the SIM7000 module. In this case there is a python-serial library that will simplify the communication with the module. However, initially there is a possibility that the device might not respond to commands, this is mostly due to a power issue. This is why standard USB port on laptops/desktops might not be enough to power the device. The recommendation is to first give it 10-15 minutes and see if it responds, if not would recommend trying a different power source. The best result was achieved by using a power brick, but YMMV. During this testing phase it is not practical to run the actual python code as there are already tools for sending UART commands.
Please run the following to install minicom.
sudo apt-get install minicom -Y
Once minicom is installed please run it by specifying the device and baudrate you want to use as well.
minicom -D /dev/ttyS0 -b 115200
Once in, for first time usage please note that to exit press [CTRL]+[A] -> [Z] (Note: not all three together, first two combo, then last key). This is crucial because if the device is not working then screen will be blank and you will not be able to get out, this should save you from that panic attack. For better understanding of what is going on, please press [CTRL]+[A] -> [E] to enable echo and this should allow you to see that the commands are being sent, just no response. For basic tests to see that the device is at least responding, please try the command AT in the minicom window/terminal. This should return OK. Once this is verified we can move onto the next step: Running the Code.
