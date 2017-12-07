import http.client
import json
import requests.packages.urllib3
import sys
import os
import time
from pyfiglet import figlet_format
import arrow
import argparse
import csv
from subprocess import Popen

# =================================================================================

'''
====================================================================================
# Requirements
------------------------------------------------------------------------------------

Pip install the following:
    - json
    - http2
    - pyfiglet
    - arrow
    - argparse
    - csv

------------------------------------------------------------------------------------
'''
# ====================================================================================
# GLOBALS
# ------------------------------------------------------------------------------------

requests.packages.urllib3.disable_warnings()

parser = argparse.ArgumentParser(description='ZSCALER API Demo Script')
parser.add_argument('-c','--Cookie',help='JSESSIONID Credential JSON file', required=True)
# parser.add_argument('-c','--credentials',help=' ZSCALER Credential  file', required=True)
parser.add_argument('-u','--url',help='URL of ZSCALER Cluster', required=True)
# parser.add_argument('-a','--admin',help='User Role', required=False, action='store_true')
args = vars(parser.parse_args())


'''
====================================================================================
Debugging function to print formatted json

Variables:
    - target: json object to be printed
------------------------------------------------------------------------------------
'''

def PrettyPrint(target):
    print (json.dumps(target,sort_keys=True,indent=4))

def Pause():
    print('Press {enter} or Type "s" to cancel the API call')
    response = input("")
    # Type "s{enter}" to skip the API call
    return True if response is not "s" else False

def ClearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

'''
====================================================================================
Authentication Headers 
------------------------------------------------------------------------------------
'''
conn = http.client.HTTPSConnection(args["url"])

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'cookie': args["Cookie"]
    }

'''
====================================================================================
Get a list WhiteListed URLs
------------------------------------------------------------------------------------
'''
def WhitelistedURLs():
	ClearScreen()
	print (figlet_format('Show Whitelisted URLs', font='small'))

	conn.request("GET", "/api/v1/security", headers=headers)

	res = conn.getresponse()
	data = res.read()

	PrettyPrint(json.loads(data.decode()))
#	print(data.decode("utf-8")) 
	Pause()

'''
====================================================================================
Get a list of BlackListed URLs
------------------------------------------------------------------------------------
'''
def BlacklistedURLs():
	ClearScreen()
	print (figlet_format('Show BlackListed URLs', font='small'))

	conn.request("GET", "/api/v1/security/advanced", headers=headers)

	res = conn.getresponse()
	data = res.read()

	PrettyPrint(json.loads(data.decode()))
#	print(data.decode("utf-8")) 
	Pause()

'''
====================================================================================
Create WhiteListed URL. 
------------------------------------------------------------------------------------
'''
def CreateWhiteListedURLs():
	ClearScreen()
	print (figlet_format('Create Whitelist', font='small'))
	payload = {  
		"whitelistUrls":[  
			"zscaler.com",
			"bringatrailer.com"
   		]
	}
	conn.request("PUT", "/api/v1/security", json.dumps(payload), headers)


	res = conn.getresponse()
	data = res.read()

	PrettyPrint(json.loads(data.decode()))
#	print(data.decode("utf-8")) 
	Pause()

'''
====================================================================================
Create BlackListed URL. 
------------------------------------------------------------------------------------
'''
def CreateBlackListedURLs():
	ClearScreen()
	print (figlet_format('Create Black List', font='small'))
	payload = {  
		"blacklistUrls":[  
			"president.ir",
			"malware.com",
			"timewaster.com"
   		]
	}
	conn.request("PUT", "/api/v1/security/advanced", json.dumps(payload), headers)

	res = conn.getresponse()
	data = res.read()

	PrettyPrint(json.loads(data.decode()))
#	print(data.decode("utf-8")) 
	Pause()

'''
====================================================================================
Add to BlackListed URL. 
------------------------------------------------------------------------------------
'''
def AddBlackListedURLs():
	ClearScreen()
	print (figlet_format('Add to Black Listed URLs', font='small'))

	payload = {  
		"blacklistUrls":[  
			"ashleymadison.com",
			"tinder.com"
   		]
	}
	conn.request("POST", "/api/v1/security/advanced/blacklistUrls?action=ADD_TO_LIST", json.dumps(payload), headers)


	res = conn.getresponse()
	data = res.read()

	print(data.decode("utf-8")) 
	Pause()


'''
====================================================================================
Delete WhiteListed URL. 
------------------------------------------------------------------------------------
'''
def DeleteWhiteListedURLs():
	ClearScreen()
	print (figlet_format('Delete White List', font='small'))
	payload = {  
		"whitelistUrls":[]
	}
	conn.request("PUT", "/api/v1/security", json.dumps(payload), headers)


	res = conn.getresponse()
	data = res.read()

	PrettyPrint(json.loads(data.decode()))
#	print(data.decode("utf-8")) 
	Pause()

'''
====================================================================================
Define Tests that need to run
------------------------------------------------------------------------------------
'''

#WhitelistedURLs()
#CreateWhiteListedURLs()
#WhitelistedURLs()
#DeleteWhiteListedURLs()
BlacklistedURLs()
CreateBlackListedURLs()
BlacklistedURLs()
AddBlackListedURLs()
BlacklistedURLs()



