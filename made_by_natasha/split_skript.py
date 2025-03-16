stroka='C:/Users/Admin/Desktop/new/rgethrt.txt'
slash=stroka.split('/')
slash[-1]='new_txt.txt'
print(slash)
new_stroka='/'.join(slash)
print(new_stroka)