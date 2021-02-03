Introduction:


https://www.cyberciti.biz/faq/find-out-linux-serial-ports-with-setserial/

## Display Detected System’s Serial Support Under Linux
dmesg | grep tty


dmesg

$ dmesg
## use grep command/egrep command to filter out USB devices ##
$ dmesg | grep -i serial
$ dmesg | grep -i FTDI

## Use the setserial command to check and use serial ports

$ sudo apt install setserial

## Using setserial to list serial ports and devices
$ sudo setserial -g /dev/ttyS[0123]

## Listing or displaying USB serial ports on Linux

$ sudo setserial -g /dev/ttyUSB[01]
