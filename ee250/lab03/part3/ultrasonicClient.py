# Ultrasonic Sensor Client
# 
# This code runs on the Raspberry Pi. It should sit in a loop which reads from
# the Grove Ultrasonic Ranger and sends the reading to the Ultrasonic Sensor 
# Server running on your VM via UDP packets. 

import sys
# By appending the folder of all the GrovePi libraries to the system path here,
# we are able to successfully `import grovepi`
sys.path.append('../../../Software/Python/')

# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

import grovepi

import socket

def Main():
    # Change the host and port as needed. For ports, use a number in the 9000 
    # range. 
    host = '192.168.1.20'
    port = 5001

    server_addr = '192.168.0.147'

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    s.bind((host,port))

    # UDP is connectionless, so a client does not formally connect to a server
    # before sending a message.
    dst_port = 8050
    while True:
        #tuples are immutable so we need to overwrite the last tuple
        server = (server_addr, int(dst_port))

        ultrasonic = grovepi.ultrasonicRead(ultrasonic_ranger)

        # for UDP, sendto() and recvfrom() are used instead
        s.sendto(ultrasonic.encode('utf-8'), server) 
        print("RPi: " + ultrasonic + " cm")
        dst_port = input("destination port-> ")
        time.sleep(0.2)
    s.close()

if __name__ == '__main__':
	Main()
    
