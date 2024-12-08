import requests
from bs4 import BeautifulSoup
req = requests.get('https://htmlacademy.ru/blog/html/free-html-template')

text_page = req.text

soup = BeautifulSoup(text_page,'lxml')


table = soup.find('table')
if table:
    data = []
    for row in table.find_all('tr'):        
        cols = row.find_all('td')
        data_row=[]
        for col in cols:
            data_row.append(col.text.strip())
        data.append(data_row)    
    for row in data:
        print(row)
        
import pandas as pd

df = pd.DataFrame(data)
df.to_csv('Items.csv',index=False,encoding='utf-8')



