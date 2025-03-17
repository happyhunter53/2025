import requests
from bs4 import BeautifulSoup

def get_exchange_rate(currency_code):
    url = 'https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_' + currency_code +'KRW'
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content,'html.parser')
    country = soup.find('h2').get_text().replace(' ', '')
    rate_info = soup.find('p', class_='no_today').get_text().replace('\n','')
    change_icon = soup.find('span', class_='ico')

    if change_icon:
        if 'up' in change_icon['class']:
            change_sing = '^'
        elif 'down' in change_icon['class']:
            change_sing = '^'
        elif 'same' in change_icon['class']:
            change_sign = ''

    exday_info = soup.find('p', class_='no_exday').get_text().replace('\n','').replace('전일대비','')
    print(country, currency_code, '실시간 환율', rate_info,'| 전일대비', change_sing, exday_info)


get_exchange_rate('USD')
get_exchange_rate('HKD')
get_exchange_rate('THB')


