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
Get Users 
------------------------------------------------------------------------------------
'''
def GetUsers():
	ClearScreen()
	print (figlet_format('Get User CSV', font='small'))
	conn.request("GET", "/api/v1/users?page=1&pageSize=100", headers=headers)

	res = conn.getresponse()
	data = res.read()

	PrettyPrint(json.loads(data.decode()))
	Pause()
'''
====================================================================================
Create Users 
------------------------------------------------------------------------------------
'''
def CreateUsers():
	payload = {  
	    "name":"Sophia Ostermiller",
	    "email":"sophia@jostermiller.zscloud.net",
        "password":"Sup3rS3cur3!",
	    "groups": [
	        { 
	        "id": 5645584,
	        "name": "Family"
	    	}
	    ],
	    "department": {
	        "id": 5645590,
	        "name": "HouseHold"
	      },

	    "comments":"family",
	    "adminUser": "false"
	}

	conn.request("POST", "/api/v1/users", json.dumps(payload), headers)

	res = conn.getresponse()
	data = res.read()

	print(data.decode("utf-8"))

	Pause()
'''
====================================================================================
Get User Annotation CSV
------------------------------------------------------------------------------------
'''
'''
def GetUserCSV():
    # Get Roles
    ClearScreen()
    print (figlet_format('Get User CSV', font='small'))

    snippet = """
file_path = 'output.csv'
resp = rc.download(file_path, '/Users/jostermi/Documents/')
p = Popen(file_path, shell=True)

    """

    print(snippet)
    file_path = 'output.csv'
    conn.request("GET", "/api/v1/users?page=1&pageSize=100", headers=headers)

#    resp = rc.download(file_path, '/Users/jostermi/Documents/')

    if resp.status_code != 200:
        print (resp.status_code)
        print (resp.text)
    else:
        print ("Download successful, opening csv...")
#        p = Popen(file_path, shell=True)
    Pause()
'''


'''
====================================================================================
Get Departments 
------------------------------------------------------------------------------------
'''
def GetDepartments():

	ClearScreen()
	print (figlet_format('Get Departments', font='small'))

	conn.request("GET", "/api/v1/departments", headers=headers)

	res = conn.getresponse()
	data = res.read()

	PrettyPrint(json.loads(data.decode()))

	Pause()

'''
====================================================================================
Get Groups 
------------------------------------------------------------------------------------
'''
def GetGroups():

	ClearScreen()
	print (figlet_format('Get Groups', font='small'))

	conn.request("GET", "/api/v1/groups", headers=headers)

	res = conn.getresponse()
	data = res.read()

	PrettyPrint(json.loads(data.decode()))

'''
====================================================================================
Define Tests that need to run
------------------------------------------------------------------------------------
'''

GetUsers()
CreateUsers()
#GetDepartments()
#GetGroups()
#GetUserCSV()

