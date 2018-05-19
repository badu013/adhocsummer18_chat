#!/usr/bin/python2
import socket,time
rec_ip="127.0.0.1"
my_port=9999
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((rec_ip,my_port))
while True:
	print s.recvfrom(1000) 
	time.sleep(1)

