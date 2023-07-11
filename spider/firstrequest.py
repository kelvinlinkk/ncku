import requests
#先將欲發出 GET 請求的網址先存在 url
url = 'https://kelvinlinkk.github.io/home.html' 
#對 url 發出 GET 請求，並將 Response 物件存在 res
res = requests.get(url)
 
print(type(res), res)
 
#Output: <class 'requests.models.Response'> <Response [200]>
