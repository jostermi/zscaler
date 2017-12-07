#zscaler
using the documentation from https://help.zscaler.com/zia/api I created a group of simple programs. 
Activate.py allows you to check on the status of the configuration as well as allows you to execute those changes. 
Audit.py allows you to create and audit log, validate the status of the audit log and download. For this example we are only looking back one hour for the audit log. Currently downloading the audit log is broken. 
DefineUserMagagement.py this program allows you to look at groups, departments, users, create users, and delete users. 
URL.py is a simple program to look at URL catagories, create a new custom URL catagory, add URLs to the custom catagory, and validate URLs for which catagory they should be in. 
These are just samples to help reduce time. 
To Execute all of these programs 
-u to define the Zscaler cloud that you are configured on 
-c to pass the jsession ID. 

for example 
        python3 Security.py -u admin.zscloud.net -c JSESSIONID=6088D7E771AD061D8B08DDB2F155ABCD
        
The JSESSIONID is created by this code snippit. 

        seed = 'API Key from the GUI'
        now = int(time.time() * 1000)
        n = str(now)[-6:]
        r = str(int(n) >> 1).zfill(6)
        key = ""
        for i in range(0, len(str(n)), 1):
            key += seed[int(str(n)[i])]
        for j in range(0, len(str(r)), 1):
            key += seed[int(str(r)[j])+2]

        print("Timestamp:", now, "\tKey", key)

        conn = http.client.HTTPSConnection("admin.zscloud.net")

        payload = {
          "username":"username",
          "password":"password",
          "timestamp":now,
          "apiKey":key
          }
        print(payload)

        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache"
            }

        conn.request("POST", "/api/v1/authenticatedSession", json.dumps(payload), headers)

        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))
