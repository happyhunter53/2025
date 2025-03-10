import requests 
import pandas as pd
from bs4 import BeautifulSoup

news = requests.get('https://finance.naver.com/news/mainnews.naver?date=20250305&page=1')
news.content


def make_urllist(page_num, )