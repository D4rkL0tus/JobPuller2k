"""
===========================================================
JobPuller2k was created with the intention of
automating and making finding specific jobs 
that are poseted and live with ease.

My goal with this software is to make job searchers
lives easier.

This software will start with very basic
I/O and no graphical user interfaces. 

This software does and will NOT have any warrenty or 
support other than the GitHub bug submitters.

This program is not meant for production useage.

USE THIS PROGRAM AT YOUR OWN RISK!
YOU HAVE BEEN WARNED AND ADVISED!
"""

# Import package files
import requests
import threading
import time
import subprocess
import json


# Class utilized for managing rqeuests with the web servers
class RequestMethods():
	
# Class utilized for managing SMTP
class EmailMethods():
	
	
# Class utilized for system check functions
class SystemCheck():
	
	def pingreq(A_Record, IPv4):
		try:
			subpr

def main():
	# File must be named JobFile.json!!
	JsonJobFile = ./JobFile.json
	# File must be named URLFile.json!!
	JsonURLFile = ./URLFile.json
	
	BANNER = """
			JobPuller2k
		Created by Stuxnet
	"""
	try:
		SystemCheck()
	except:
		print("The system check pointed to issues with the application")
		print("Exiting...")
		time.sleep(3)
		exit()
	
def SystemCheck():
	DNSName = "one.one.one.one"
	ARecord = "1.1.1.1"
	
	print("Checking Internet Connectivitiy")
	
	# Simple ICMP ping to both a domain, and a A Record
	try:
		SystemCheck.pingreq(DNSName, ARecord)
	except:
		print("There was an issue with connecting to the internet,\nplease check your connection and try again")
		time.sleep(3)
		exit()
		
		
		
	
if __name__ == "__main__":
	main()
