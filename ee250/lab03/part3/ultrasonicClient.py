# EE 250 Lab 3
#
# Github Repo:
#	
# Team Members: 
#	Jeffrey Loh
#	Martin Romo

# Ultrasonic Sensor Client
# 
# This code runs on the Raspberry Pi. It should sit in a loop which reads from
# the Grove Ultrasonic Ranger and sends the reading to the Ultrasonic Sensor 
# Server running on your VM via UDP packets. 

import sys
import time
# By appending the folder of all the GrovePi libraries to the system path here,
# we are able to successfully `import grovepi`
sys.path.append('../../../Software/Python/')

import grovepi
import socket

def startClient():
    # Change the host and port as needed. For ports, use a number in the 9000 
    # range. 
    host = '192.168.1.20' # RPI IP Address
    port = 5001 # Port to use

    server_addr = '192.168.0.147' # Host OS IP Address
	server_port = 8050

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    s.bind((host,port))

    # Grove Ultrasonic Ranger connected to digital port D2
    ultrasonic_ranger = 2
	
    server = (server_addr, server_port)
    while True:
		# Get ultrasonic reading
		ultrasonic = grovepi.ultrasonicRead(ultrasonic_ranger)
        msg = str(ultrasonic)
		
        # for UDP, sendto() and recvfrom() are used instead
        s.sendto(msg.encode('utf-8'), server) 
        print("RPi: " + msg + " cm") # Print reading on client terminal
        time.sleep(0.2)
    s.close()

if __name__ == '__main__':
    startClient()
