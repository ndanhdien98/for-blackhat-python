#!/usr/bin/env python3
import socket
import subprocess
import sys
from datetime import datetime

#Clear screen
subprocess.call('clear', shell=True)

#Ask for input
remoteServer = input("Enter a remote host to scan:  ")
remoteServerIp = socket.gethostbyname(remoteServer)

#Print banner
print ("-" * 60)
print ("Cho ti, dang scan", remoteServerIp)
print ("-" * 60)

#Check what time scan started
t1 = datetime.now()

#Using the range function to specify ports (here it will scans all ports betweeen 1 and 1024)

#We also put in some error handling for catching errors
try:
	for port in range(1,1025):
		soc = socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex(remoteServerIp,port)
		if result ==  0:
			print ("Port {}:       Open".format(port))
		sock.close()
except KeyboardInterrupt:
	print ("You press Ctrl+C")
	sys.exit()

except socket.gaierror:
	print ("Hostname could not be resolved. Exiting")
	sys.exit()

except socket.error:
	print ("Couldn't connect to server")
	sys.exit()

#Checing time again
t2 = datetime.now()

#Calculates the difference of time, to see how long it took to run the script
total = t2 - t1

#Printing the infomation to screen
print ("Scanning completed in; ", total)
