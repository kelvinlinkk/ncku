from bs4 import BeautifulSoup
import requests
import json

result = []
def crawlers(url, count):
    if count == 0:
        return
    global result
    txt = requests.get(url).text
    soup = BeautifulSoup(txt, 'html.parser')

    elems = soup.find_all(class_='r-ent')
    last_page = soup.find_all(class_='btn wide')[1]['href']
    for elem in elems:
        if elem.find('a') == None:
            continue
        result.append({
            "title": elem.find(class_= 'title').getText(),
            "attr":elem.find('a')['href'],
            "author":elem.find(class_= 'author').getText(),
            "date":elem.find(class_ = 'date').getText()
        })
    print("剩下" + str(count-1) + "頁")
    crawlers('https://www.ptt.cc' + last_page, count-1)
crawlers('https://www.ptt.cc/bbs/Baseball/index.html', int(input("要抓PTT棒球板幾頁：")))
print("完成！")
with open('baseball.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=2, sort_keys=True, ensure_ascii=False)
