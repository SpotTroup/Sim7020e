  import time
	import hashlib
	

	# define constants
	SERIAL_DEVICE = '/dev/ttyS0' # for pi zero w
	# SERIAL_DEVICE = '/dev/ttyAMA0' # for pi 3+ 
	BAUD_RATE = 115200 # for SIM7000 family
	# BAUD_RATE = 9600 # for SIM800 family
	TIMEOUT = 10 # wait for 10 seconds before giving up on a command (it is high to account for the GPS latency)
	ENTER_KEY = '\r\n'

	

	def send_command(cmd):
	    # Define serial device
	    sr_dev = serial.Serial(SERIAL_DEVICE, baudrate=BAUD_RATE, timeout=1)
	    # Transmit command to the SIM Module
	    sr_dev.write(cmd.encode()+ENTER_KEY.encode)
	    # Receive output from the SIM Module
	    rxbuffer = sr_dev.read(len(cmd)) # this will be the echo of the command
	    print(rxbuffer)
	    rxbuffer = sr_dev.read(100) # read the max characters allowed
	    print(rxbuffer)
	    print(sr_dev.read(100)) # read any additional characters to empty out buffer
	    time.sleep(5)
	    return rxbuffer
	

	

	if __name__ == "__main__":
	    
	    while True:
          val = input("Enter your AT command: ") 
	        send_command(val)
	        time.sleep(300)
