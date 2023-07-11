import requests
import json
#先將欲發出 GET 請求的網址先存在 url
url = 'http://dev.vincent55.tw/json' 
#對 url 發出 GET 請求，並將 Response 物件透過 json 解析後存在 res
res = requests.get(url).json()
print(type(res), res)
print(res['slideshow']['slides'][1]['title'])
 
# 將回傳值存於 result.json
with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(res, f, indent=2, sort_keys=True, ensure_ascii=False)
 
'''
<class 'dict'> {'slideshow': {'author': 'Yours Truly', 'date': 'date of publication', 'slides': [{'title': 'Wake up to WonderWidgets!', 'type': 'all'}, {'items': ['Why <em>WonderWidgets</em> are great', 'Who <em>buys</em> WonderWidgets'], 'title': 'Overview', 'type': 'all'}], 'title': 'Sample Slide Show'}}
Overview
'''

# 讀取json檔案
url ='test.json'
with open(url, 'r') as result_fd:
    result_file = json.load(result_fd)
    print(result_file['info'])

