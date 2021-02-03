## GENERAL COMMANDS
- apt-get update
- apt-get upgrade
- find / -name example.txt: Searches the whole system for the file example.txt and outputs a list of all directories that contain the file.
-poweroff: To shutdown immediately.
-raspi-config: Opens the configuration settings menu.
-reboot: To reboot immediately.
- shutdown -h now: To shutdown immediately. // shutdown -h 01:22: To shutdown at 1:22 AM.
-startx: Opens the GUI (Graphical User Interface)


## FILE AND DIRECTORY COMMANDS
- cat example.txt: Displays the contents of the file example.txt.
- cp /home/pi/documents/examplefile.txt /home/pi/office/
- ls -l: Lists files in the current directory, along with file size, date modified, and permissions.
- mv examplefile.txt /home/pi/office/ 
-rm example.txt: Deletes the file example.txt.
-rmdir example_directory: Deletes the directory example_directory (only if it is empty).

## NETWORKING AND INTERNET COMMANDS

- ifconfig: To check the status of the wireless connection you are using (to see if wlan0 has acquired an IP address).
-iwconfig: To check which network the wireless adapter is using.
-iwlist wlan0 scan: Prints a list of the currently available wireless networks.
-iwlist wlan0 scan | grep ESSID: Use grep along with the name of a field to list only the fields you need (for example to just list the ESSIDs).
-nmap: Scans your network and lists connected devices, port number, protocol, state (open or closed) operating system, MAC addresses, and other information.
-ping: Tests connectivity between two devices connected on a network. For example, ping 10.0.0.32 will send a packet to the device at IP 10.0.0.32 and wait for a response. It also works with website addresses.
-wget http://www.website.com/example.txt: Downloads the file example.txt from the web and saves it to the current directory


## SYSTEM INFORMATION COMMANDS
-df -h: Shows information about the available disk space.
-df /: Shows how much free disk space is available.
-dpkg - -get-selections | grep XXX: Shows all of the installed packages that are related to XXX.
-dpkg - -get-selections: Shows all of your installed packages
-free: Shows how much free memory is available.
-hostname -I: Shows the IP address of your Raspberry Pi.
-lsusb: Lists USB hardware connected to your Raspberry Pi.
-vcgencmd measure_temp: Shows the temperature of the CPU.
-vcgencmd get_mem arm && vcgencmd get_mem gpu: Shows the memory split between the CPU and GPU.
