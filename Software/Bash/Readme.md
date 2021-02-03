## Everything to Scripts 4 AutoStart

## How To 
https://www.circuitbasics.com/how-to-write-and-run-a-shell-script-on-the-raspberry-pi/


http://www.netzmafia.de/skripten/hardware/RasPi/RasPi_Auto.html

first of all create the script for me it's startup_file.sh

move startup_file.sh to /etc/init.d/

make sure it is executable by : sudo chmod +x /etc/init.d/startup_file.sh

now use this command: sudo update-rc.d startup_file.sh defaults

this one was suggested by goldilocks:

sudo update-rc.d /etc/init.d/startup_file.sh defaults ; it didn't work for me !!

just try one of the two should work
