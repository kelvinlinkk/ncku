from bs4 import BeautifulSoup
import requests
import os

url = 'https://csie.ncku.camp'
txt = requests.get(url).text
soup = BeautifulSoup(txt,'html.parser')
# print(soup.prettify())
# print(soup.find_all('img')[0]["src"][1:])
print(soup.find_all('h1', class_='title'))
os.system('wget ' + url + soup.find_all('img')[0]["src"][1:])
'''html_text = """
<html><head></head><body><h1>Hello, World!</h1></body></html>
"""
soup = BeautifulSoup(html_text, "html.parser")
print(soup.prettify())
'''