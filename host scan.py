#!/usr/bin/python3
import socket
while 1:
 a=int(input("options 1 remote ip, options 2 local ip ,options 3 exist\n: ") )
 if a==1:
 	host=input("Enter your host: ")
 	print("device host name >>"+socket.gethostname())
 	print("remote host name >>"+socket.gethostbyname(host))
 elif 2:
 	try:
 		lhost=socket.gethostname()
 		ip_address=(socket.gethostbyname_ex(lhost))
 		print(str("device ip >>"+ip_address[2][0]))
 	except:
 		print("Error")
 elif a==3:
 	quit()
 else:
 	print("wrong input ")