#Ultrasonic Sensor Server
#
# This code runs on your VM and receives a stream of packets holding ultrasonic
# sensor data and prints it to stdout. Use a UDP socket here.

import socket

def startServer():
    # Change the host and port as needed. For ports, use a number in the 9000 
    # range. 
    host = '10.0.2.15'
    port = 9000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))

    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("VM: " + data + " cm")
    c.close()


if __name__ == '__main__':
    startServer()
    