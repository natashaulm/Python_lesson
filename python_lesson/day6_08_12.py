

from bs4 import BeautifulSoup

file_path = rf"C:\Users\levsh\Desktop\git\Python_lesson\python_lesson\web_site.html"


#Home 
#1 Нужно открыть файлы, которые я передам, записать данные в переменные
#2 Нужно презаписать файл и добавить в него текст
#3 Нужно открыть файл, но если его нет, то создать
#4 Нужно добавить текст в конец файла, не перезаписывая
with open(file_path,'r',encoding='utf-8') as file:
    html_content = file.read()
    
soup = BeautifulSoup(html_content,'lxml') 

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

else:
    print('not found')