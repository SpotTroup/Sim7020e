Documentation for the sim7000:
https://support.hologram.io/hc/en-us/articles/360036559494-SIMCOM-SIM7000
Documentation: 
https://simcom.ee/documents/SIM7020/SIM7020%20Series_MQTT%28S%29_Application%20Note_V1.03.pdf
-> 3.2 APN manual setting

To Set-UP:
APN: hologram
APN username: (none)
APN password: (none)
IP Address: Dynamic (using DHCP)
Data Roaming: Enabled

screen /dev/ttyUSB2
A new Terminal window will open. Use the following command to determine if the correct dev path was chosen:

AT
Expected Response: OK

AT+CFUN=1
Expected Response: OK
It may help to run the following commands to ensure the device recognizes LTE networks. This is especially true with the SIM7000G model.

//Set preferred mode to LTE only.
AT+CNMP=38
Expected Response: OK

//Set device preference to Cat-M1 over NB-IoT
AT+CMNB=1
Expected Response: OK
