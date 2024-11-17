import requests
from bs4 import BeautifulSoup
req = requests.get('https://www.sport1tv.ru/figurnoe-katanie')

text_page = req.text


soup = BeautifulSoup(text_page,'lxml')
print(soup)


print('Заголовки страницы')
print(soup.header)


