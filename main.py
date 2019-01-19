
import requests
from bs4 import BeautifulSoup
from time import sleep

short = input('Short name of company(e.g CCC or LPP): ')
source = 'https://www.bankier.pl/inwestowanie/profile/quote.html?symbol='

while True:
    data = requests.get(source+short)
    data.encoding = 'utf-8'
    soup = BeautifulSoup(data.text, 'html.parser')
    latestprice = soup.find('div', {'class': 'profilLast'}).text.strip()
    print(latestprice, end='\r')
    sleep(30)
    data = None
