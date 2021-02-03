#!/usr/bin/python

import Jetson.GPIO as GPIO
import serial
import time

ser = serial.Serial("/dev/ttyTHS1",115200)
ser.flushInput()

command_input = ''
rec_buff = ''

try:
    while True:
        print("press Ctrl+C to exit")
        command_input = input('Please input the AT command:')
        ser.write((command_input + '\r\n').encode())
        time.sleep(0.1)
        if ser.inWaiting():
            time.sleep(0.01)
            rec_buff = ser.read(ser.inWaiting())
        if rec_buff != '':
            print(rec_buff.decode())
            rec_buff = ''
except:
    if ser != None:
        ser.close()
