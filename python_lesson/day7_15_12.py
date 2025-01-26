# 1 - open FileExist
# 2 - read write update
# 3 - close

# txt, rtf, bin 
# json, csv, db

## docx, pdf, (latex - never)

# 1 open

# file_path = 'bloknot.txt'
# file = open(file_path,'r',encoding='utf-8')
# try:
#     print(*file)
#     print(16/0)
# except Exception as ex:
#     print(ex)
# finally:
#     file.close()    
    
# print(*file) 
# file.close()

# with open('bloknot.txt','r') as file:
#     print(file.read(5))
#     print(file.tell())
#     file.seek(0,0)
#     print(file.tell())
#     print(file.read(3))

# import os 
# os.rename('bloknot.txt','to-do_list.txt')


#csv
# import csv
# with open('items.csv','r',encoding='utf-8') as file:
#     csvreader = csv.reader(file)
#     for row in csvreader:
#         print(row)





# Словарь в json файле 300 слов
# Структура словаря: 1:{'eng':word,'rus':слово} ...

import json 
# with open('json_file.json') as file:
#     data =json.load(file)
#     print(data['glossary']['title'])


data = [{'name':'Oleg','age':10},{'name':'Andrew','age':20}]

with open("json_test.json",'w') as file:
    json.dump(data,file)

with open('json_test.json') as file:
    data =json.load(file)
    print(data[0])
