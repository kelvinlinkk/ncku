import requests
#先將欲發出 GET 請求的網址先存在 url
url = 'https://csie.ncku.camp/' 
#對 url 發出 GET 請求，並將 Response 物件存在 res
res = requests.get(url)
print(res.text)
# 網頁內容
