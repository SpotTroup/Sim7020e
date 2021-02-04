#!/bin/bash

## TODO: make it autorun the nano change de_DE.UTF-8 UTF-8 -> en_US.UTF-8 UTF-8

sudo nano /etc/default/keyboard

XKBMODEL=pc105
XKBLAYOUT=us
XKBVARIANT=
XKBOPTIONS=
BACKSPACE=guess



sudo dpkg-reconfigure locales 

sudo dpkg-reconfigure tzdata


