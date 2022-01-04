#!/usr/bin/python3
#small calculator program
#2022.1.4
#programmer la pyae maung maung
fast=0
second=0
while 1:
 fast=int(input("Enter your fast number: "))
 second=int(input ("Enter your second number: "))
 operator=input("Enter your operator: ")
 if operator=='+':
	 result=fast+second
 elif operator=='-':
  	result=fast-second
 elif operator=='*':
      result=fast*second
 elif operator=='%':
      result=fast%second
 elif operator=='//':
      result=fast//second
 else :
 	 print("wrong input try again ")
 print("results: ",result)