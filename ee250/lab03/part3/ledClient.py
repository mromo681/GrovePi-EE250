# EE 250 Lab 3
#
# Github Repo:
#	
# Team Members: 
#	Jeffrey Loh
#	Martin Romo

# LED Client 
#
# This code runs on yoru VM and sends requests to the Raspberry Pi to turn on 
# and off the Grove LED using TCP packets.
import socket

def startClient():
	host = '192.168.1.20' # RPI IP
	port = 5000 #Port to use

	s = socket.socket() # by default, the socket constructor creates an TCP/IPv4 socket
	s.connect((host,port))

	message = input("-> ") # Prompt client for command
	while message != 'q':
		s.send(message.encode('utf-8')) 
		#1024 is the receive buffer size. It's enough for us, and it's a nice number. 
		data = s.recv(1024).decode('utf-8') 
		print(data) # Print response from server
		message = input("-> ") # Prompt client for command
	s.close()

if __name__ == '__main__':
	startClient()