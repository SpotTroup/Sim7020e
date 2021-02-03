##########################################################################################################################################
'''
 ____  _          _____ ___ ____   ___
/ ___|(_)_ __ ___|___  / _ \___ \ / _ \  ___
\___ \| | '_ ` _ \  / / | | |__) | | | |/ _ \
 ___) | | | | | | |/ /| |_| / __/| |_| |  __/
|____/|_|_| |_| |_/_/  \___/_____|\___/ \___|
                                                       '''
##########################################################################################################################################
# Name: howtoinstall.md 
# Comments: install 
# Author: Alam al Saud + Tjark Ziehm
# Version: 0.1
# Data: February 2020
# Basic: python3
# needs: Todo Tree, ...
#######################Features###########################################################################################################
# TODO:
# FIXME:
#######################Index##############################################################################################################
# 1. Update Firmware 
# 2. Install needed RPI header
# 3. Update Raspian & activate the Hardware Serial 
# 4. Download Testfiles
# 5. Configure System 
##########################################################################################################################################

## 1. Update Firmware:
$ sudo rpi-update
$ rpi-source



## 2. Install needed RPI header
sudo apt-get install linux-image-rpi-rpfv linux-headers-rpi-rpfvsudo apt-get install linux-image-rpi-rpfv linux-headers-rpi-rpfv

## 3. Update Raspian & activate the Hardware Serial 
$ sudo apt-get update
$ sudo apt-get install upgrade -Y

# enable hardware serial:
# Once everything is updated and the device is ready, please start validating that UART is enabled.
*	sudo raspi-config
*	option 5 - interfacing options
*	option P6 - serial
*	Would you like a login shell to be accessible over serial? -> No
*	Would you like the serial port hardware to be enabled? -> Yes

# Controll it and restart 
controll:
$ sudo nano /boot/config.txt -> enable_uart=1  
then:
$ reboot

# Important:
With UART configured please check whether or not you see the device we will be interfacing with /dev/ttyS0 with command: 
4 ls -l /dev | grep tty.

## 4. Download Testfiles
$ cd Downloads
$ sudo git clone https://github.com/SpotTroup/Sim7020e
## FIXME: change foldername from c++ Code without  space
$ cp Downloads/Sim7020e/Hardware/SIM7020/TestCode/Raspberry/SIM7020X to /home/pi/
$ cd ./home/pi//SIM7020X/
$ chmod 777 sim7020_nbiot_hat_init

## 5. Configure System
# Modify rc.local file:

$ sudo nano /etc/rc.local

# Add to last line before
$ sh /home/pi/SIM7020X/sim7020_nbiot_hat_init  exit and change # change  $ exit 0 ->  $ exit 1



Install Minicom:
sudo apt-get install minicom
Execute minicom -D /dev/ttyS0 to enter the minicom (ttyS0: Pi 3B/3B+, ttyAMA0: Zero/2B)

Press CTRL+a then z -> e to activate echo for console
Maybe you have to start the SIMCOM Device by ressing the button.
Check$ AT you need to get the response OK

Using demo code:
cd /SIM7020X/bcm2835
Go to
cd ./home/pi//SIM7020X/bcm2835
sudo chmod 755 ./configure
./configure & make & sudo make check & sudo make install
This can take till to 15 minutes
if it fails use
autoreconf -vfi && ./configure MKDIR_P="mkdir -p"
and repeat

if it fails again:
After looking into the configure.ac script some more, it appears that a line specifying the location of the aux directory, AC_CONFIG_AUX_DIR, is the cause. Removing this seems to provide sane results for a suitable MKDIR_P value.

Now lets test:
cd /home/pi/SIM7020X/examples/AT

The following commant brings you to the Terminal for the SIMCOM for AT commands
sudo make clean && sudo make && sudo ./main

///////////////////////////////////////////////////////////////////////////////
0.uname -a

2.ls -la /lib/modules/$(uname -r)/ | grep -i build 3.

sudo wget https://raw.githubusercontent.com/notro/rpi-source/master/rpi-source -O /usr/bin/rpi-source && sudo chmod +x /usr/bin/rpi-source && /usr/bin/rpi-source -q --tag-update
