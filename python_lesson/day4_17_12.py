import requests
from bs4 import BeautifulSoup
req = requests.get('https://www.sport1tv.ru/figurnoe-katanie')

text_page = req.text

soup = BeautifulSoup(text_page,'lxml')

count=0

print(soup.div['class'])


# for i in soup.find_all("div",{"class":"title"}):
#     print(i)





