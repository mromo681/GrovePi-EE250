# LED Server
# 
# This program runs on the Raspberry Pi and accepts requests to turn on and off
# the LED via TCP packets.

import sys
import socket
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../../Software/Python/')

import grovepi

def startServer():
	# LED connected to D4
	led = 4
	grovepi.pinMode(led,"OUTPUT")
	time.sleep(1)

	host = '192.168.1.20'
	port = 5000

	s = socket.socket()
	s.bind((host,port))
	s.listen(1)
	c, addr = s.accept()
	while True:
		data = c.recv(1024).decode('utf-8')
		msg = ""
		if not data:
			break
		print("VM: "+data)
		if data == "LED_ON":
			grovepi.digitalWrite(led,1)
			msg = "LED_ON Success"
		else if data == "LED_OFF":
			grovepi.digitalWrite(led,0)
			msg = "LED_OFF Success"
		else
			msg = "Command Not Recognized"
		print("-> "+msg)
		c.send(msg.encode('utf-8'))
	c.close()

if __name__ == '__main__':
	startServer()
    