rt http.client
import json
import time
import datetime
import json
import logging
import requests
import argparse
import os
import sys
import re
from http import cookies
import urllib.parse
import httplib2

#
#import zscalerrestsdk
#from zscalerrestsdk import exceptions

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

====================================================================================
# Requirements
------------------------------------------------------------------------------------
python3 Authentication-PWD.py -u admin@domain.com -p ZSc\@l3r123 -z admin.zscloud.net -a TU44cliwYc7O
output should look like the below

Timestamp: 1512835187176 	Key UYwUwi4Olw77
JSESSIONID=B7AE7E5A282474A694652EFB5C11E829
{"authType":"ADMIN_LOGIN","obfuscateApiKey":true}

Remember you have to escape all special characters when you type in your password. To escape a 
special character use "\" before it. For example if the password was Zsc@l3r123 then you have to 
type ZSc\@l3r123 instead, notice the "\"
'''
# ====================================================================================
# GLOBALS
# ------------------------------------------------------------------------------------

requests.packages.urllib3.disable_warnings()

parser = argparse.ArgumentParser(description='ZSCALER API Demo Script')
parser.add_argument('-u','--user',help='username', required=True)
parser.add_argument('-p','--password',help='password', required=True)
parser.add_argument('-a','--api',help='api key', required=True)
parser.add_argument('-z','--zcloud',help='URL of ZSCALER Cluster', required=True)
args = vars(parser.parse_args())



def parse_jsessionid(cookie):
    jsessionid = re.sub(r';.*$', "", cookie)
    return jsessionid

seed = args["api"]
now = int(time.time() * 1000)
n = str(now)[-6:]
r = str(int(n) >> 1).zfill(6)
key = ""
for i in range(0, len(str(n)), 1):
    key += seed[int(str(n)[i])]
for j in range(0, len(str(r)), 1):
    key += seed[int(str(r)[j])+2]
 
print("Timestamp:", now, "\tKey", key)

conn = http.client.HTTPSConnection(args["zcloud"])

payload = {
	"username":args["user"],
	"password":args["password"],
	"timestamp":now,
	"apiKey":key
	}
#print(payload)

header = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }
http = httplib2.Http()
response, content = http.request("https://admin.zscloud.net/api/v1/authenticatedSession", 'POST', headers=header, body=json.dumps(payload))


cookie = response['set-cookie']
jsessionid = re.sub(r';.*$', "", cookie)
print(jsessionid)
print(content.decode("utf-8"))

