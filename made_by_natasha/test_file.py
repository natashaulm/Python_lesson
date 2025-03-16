with open('test_bloknot.txt', 'w', encoding='UTF-8') as file:
    file.write('Very сложно')


import json
data = ['фрукты', 'vegetables']
with open('test_json.json', 'w') as file:
    json.dump(data, file)
    
with open('test_json.json') as file:
    data = json.load(file)
    print(data)