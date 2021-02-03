Setting it to be run
To launch the script at start-up edit the “rc.local” file needs to be edited.


sudo nano /etc/rc.local
 

Add the following line:


/home/pi/bin/script_auto_run
Save it by pressing Ctrl+X, " Y", ENTER

Re-boot your RPi and it will run.
