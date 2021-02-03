sudo rpi-update rpi-source

sudo apt-get install linux-image-rpi-rpfv linux-headers-rpi-rpfvsudo apt-get install linux-image-rpi-rpfv linux-headers-rpi-rpfv

cp /SIM7020/TestCode/SIM7020E to /home/pi/ cd ./home/pi//SIM7020X/ chmod 777 sim7020_nbiot_hat_init

Modify rc.local file: sudo nano /etc/rc.local

Add: sh /home/pi/SIM7020X/sim7020_nbiot_hat_init to last line before exit and change exit 0 to exit 1

enable hardware serial: sudo raspi-config Choose Interfacing Options->Serial->no->yes->ok check sudo nano /boot/config.txt for enable_uart=1 reboot

Install Minicom: sudo apt-get install minicom Execute minicom -D /dev/ttyS0 to enter the minicom (ttyS0: Pi 3B/3B+, ttyAMA0: Zero/2B)

Press CTRL+a then z -> e to activate echo for console Maybe you have to start the SIMCOM Device by ressing the button. Check$ AT you need to get the response OK

Using demo code: cd /SIM7020X/bcm2835 Go to cd ./home/pi//SIM7020X/bcm2835 sudo chmod 755 ./configure ./configure & make & sudo make check & sudo make install This can take till to 15 minutes if it fails use autoreconf -vfi && ./configure MKDIR_P="mkdir -p" and repeat

if it fails again: After looking into the configure.ac script some more, it appears that a line specifying the location of the aux directory, AC_CONFIG_AUX_DIR, is the cause. Removing this seems to provide sane results for a suitable MKDIR_P value.

Now lets test: cd /home/pi/SIM7020X/examples/AT

The following commant brings you to the Terminal for the SIMCOM for AT commands sudo make clean && sudo make && sudo ./main

/////////////////////////////////////////////////////////////////////////////// 0.uname -a

2.ls -la /lib/modules/$(uname -r)/ | grep -i build 3.

sudo wget https://raw.githubusercontent.com/notro/rpi-source/master/rpi-source -O /usr/bin/rpi-source && sudo chmod +x /usr/bin/rpi-source && /usr/bin/rpi-source -q --tag-update
