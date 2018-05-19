#!/usr/bin/python2
import socket,time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
	x=raw_input("Client:")#storing client data in x
	s.sendto(x,("127.0.0.1",9999))
	time.sleep(1)
	
