import requests 
import pandas as pd
from bs4 import BeautifulSoup

page_num = 1
code = 'stock'
date = 20250305
url = 'https://finance.naver.com/news/mainnews.naver'+'?date='+str(date)+'&page='+str(page_num)

print(url)

