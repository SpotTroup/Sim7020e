#!/usr/bin/python

import Jetson.GPIO as GPIO
import serial
import time

ser=serial.Serial('/dev/ttyTHS1',115200)
ser.flushInput()

rec_buff = ''
ServerIP = '118.190.93.84'
Port = '2317'
Message = 'Waveshare Sending udp data with socket_id'

def send_at(command,back,timeout):
    rec_buff = ''
    ser.write((command+'\r\n').encode())
    time.sleep(timeout)
    if ser.inWaiting():
        time.sleep(0.1 )
        rec_buff = ser.read(ser.inWaiting())
    if rec_buff != '':
        if back not in rec_buff.decode():
            print(command + ' ERROR')
            print(command + ' back:\t' + rec_buff.decode())
            return 0
        else:
            print(rec_buff.decode())
            return 1
    else:
        print(command + ' no responce')
        return 0

try:
    if True == send_at('AT+CSOC=1,2,1','+CSOC:',0.5):
        print('Created UDP socket id Successfully!')
        send_at('AT+CSOCON=0,2317,\"118.190.93.84\"','',2)
        send_at('AT+CSOSEND=0,0,\"Waveshare Send to Socket id 0 using UDP\"','',2)
    send_at('AT+CSOCL=0','OK',0.5)
    print('Close Socket')
except:
    if ser != None:
        ser.close()
    GPIO.cleanup()
