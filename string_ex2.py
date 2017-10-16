#!/usr/bin/env python

ip_addr = input("Please enter an IP addres: ")

#print (ip_addr)
ip_addr = (ip_addr.split("."))
#print (ip_addr[0])
#print (ip_addr[1])
#print (ip_addr[2])
#print (ip_addr[3])

print('{:12}{:12}{:12}{:12}'.format (ip_addr[0], ip_addr[1], ip_addr[2], ip_addr[3]))
