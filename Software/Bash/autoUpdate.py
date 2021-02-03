##########################################################################################################################################
'''
 ____  _          _____ ___ ____   ___       
/ ___|(_)_ __ ___|___  / _ \___ \ / _ \  ___ 
\___ \| | '_ ` _ \  / / | | |__) | | | |/ _ \
 ___) | | | | | | |/ /| |_| / __/| |_| |  __/
|____/|_|_| |_| |_/_/  \___/_____|\___/ \___|
                                                       '''
##########################################################################################################################################
##  Name:autoUpdate.py
##  Comments: Test file to use python with terminal power
##  Author: Tjark Ziehm
##  Version: 0.1
##  Data: February 2020
##  Basic: python3
##  needs: Todo Tree, ...
#######################Features###########################################################################################################
## TODO:
## FIXME:
#######################Index##############################################################################################################
##  1.
##  2. ...
##########################################################################################################################################

#!/usr/bin/pyhthon3
import subprocess
import sys

resturncode = subprocess.call(['ls', '-l'])

resturncode = subprocess.call(['pwd'])


''' sys.executable is the absolute path, subprocess.run is given the list
To subprocess.run is passed a list of strings consisting of the components of the command we want to execute. Since the first string we pass is sys.executable, we instruct subprocess.run to run a new Python program.
The -c component is a python command line option that allows you to pass a string containing an entire Python program for execution. In our case, we pass a program that outputs the string ocean.
'''
##subprocess.run is able to run all sudo stuff !!! Warning !!!
'''resturncode = subprocess.run([sys.executable, "-c", "print('ocean')"])


result = subprocess.run(
    [sys.executable, "-c", "print('ocean')"], capture_output=True, text=True
)
print("stdout:", result.stdout)
print("stderr:", result.stderr)
'''

## with exitcode
'''result = subprocess.run([sys.executable, "-c", "raise ValueError('oops')"], check=True)'''

## Alternative return Check -> shows problem before started
'''
result = subprocess.run([sys.executable, "-c", "raise ValueError('oops')"])
result.check_returncode()
'''

## Timeout to break

'''result = subprocess.run([sys.executable, "-c", "import time; time.sleep(2)"], timeout=1)'''

### Passing input to programs
result = subprocess.run(
    [sys.executable, "-c", "import sys; print(sys.stdin.read())"], input=b"underwater"
)