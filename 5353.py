import requests 
import pandas as pd
from bs4 import BeautifulSoup

page_num = 1
code = 'stock'
date = 20250305
url = 'https://finance.naver.com/news/mainnews.naver'+'?date='+str(date)+'&page='+str(page_num)

def make_urllist(page_num, code, date):
    urllist = []
    for i in range(1, page_num + 1):
        url = 'https://finance.naver.com/news/mainnews.naver'+'?date='+str(date)+'&page='+str(page_num)
        news = requests.get(url)
        new.content

        soup = BeautifulSoup(news.content, 'heml.parser')
        news_list = soup.select('.list_allnews li div strong')
        for line in news_list:
            urllist.append(line.a.get('href'))
    return urllist


url_list = make_urllist(2, 'society', 20250305)
print('뉴스 기사의 개수 :' , len(yrl_list))

