import requests
from bs4 import BeautifulSoup

URL = 'https://www.naver.com/'
data = requests.get(URL).text
soup = BeautifulSoup(data, 'html.parser')
news_titles = soup.find_all(class_='ah_k')
title_list=[]
for title in news_titles:
    title_list.append(title.text)

print(title_list)