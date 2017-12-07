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
Audit Report Status 
------------------------------------------------------------------------------------
'''
def Activate():
	ClearScreen()
	print (figlet_format('Activate', font='small'))
	conn.request("POST", "/api/v1/status/activate", headers=headers)

	res = conn.getresponse()
	data = res.read()

#	print(data.decode("utf-8")) 
	PrettyPrint(json.loads(data.decode()))
	Pause()
'''
====================================================================================
Activation Status
------------------------------------------------------------------------------------
'''
def ActivationStatus():
	ClearScreen()
	print (figlet_format('Activation Status', font='small'))

	conn.request("GET", "/api/v1/status", headers)

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


#ActivationStatus()
Activate()

