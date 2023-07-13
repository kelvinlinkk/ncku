from bs4 import BeautifulSoup
import requests
import os

url = 'http://127.0.0.1:3000/home.html'
txt = requests.get(url).text
soup = BeautifulSoup(txt,'html.parser')
# print(soup.prettify())
# print(soup.find_all('img')[0]["src"][1:])
print(soup.find_all('h1', class_='title'))
print(soup.find_all('img')[0]['ondblclick'])
os.system('wget ' + url + soup.find_all('img')[0]["src"][1:])
'''html_text = """
<html><head></head><body><h1>Hello, World!</h1></body></html>
"""
soup = BeautifulSoup(html_text, "html.parser")
print(soup.prettify())
'''