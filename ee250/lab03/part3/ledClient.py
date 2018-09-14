# LED Client 
#
# This code runs on yoru VM and sends requests to the Raspberry Pi to turn on 
# and off the Grove LED using TCP packets.
import socket

def startClient():
    host = '10.0.2.15'
    port = 5000

    s = socket.socket() #by default, the socket constructor creates an TCP/IPv4 socket
    s.connect((host,port))

    message = input("-> ")
    while message != 'q':
        s.send(message.encode('utf-8')) 
        #1024 is the receive buffer size. It's enough for us, and it's a nice number. 
        data = s.recv(1024).decode('utf-8') 
        print(data)
        message = input("-> ")
    s.close()

"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 tcpClient.py` in terminal, this if-statement will be 
true"""
if __name__ == '__main__':
    startClient()