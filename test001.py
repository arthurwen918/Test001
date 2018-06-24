import requests
url = 'http://www.sina.cn/'
res = requests.get(url).text
print(res)
