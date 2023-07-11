import json
import requests
import os

url = 'https://api.thecatapi.com/v1/images/search'
mylist = []
os.system("rm -rf ~/桌面/ncku/spider/cats/")
num = int(input("請輸入圖片數量:"))
for i in range(num):
    res = requests.get(url)
    mylist.append(res.json()[0])
    imgURL = res.json()[0]['url']
    os.system('wget ' + imgURL + ' -P ~/桌面/ncku/spider/cats/')

with open('result.json', 'w', encoding='utf-8') as f:
    f.write("{\n")
    for i in range(num):
        f.write('  \"pic' + str(i+1) + '\":')
        json.dump(mylist[i]['url'], f, indent=2, sort_keys=True, ensure_ascii=False)
        if i != num-1:
            f.write(',\n')
    f.write("\n}")


with open('cat.json','w',encoding='utf-8') as f:
    f.write("{\n")
    for i in range(num):
        f.write('  \"pic' + str(i+1) + '\":')
        f.write('\"' + imgURL + '\"')
        if i != num-1:
            f.write(',\n')
    f.write('\n}')
