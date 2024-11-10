#4.Даны три слова 'аквариум', 'мармелад' и 'рама'. Выведите на экран сперва все виды букв, 
# которые присутствуют во всех словах сразу, а затем все виды букв, которые присутствуют 
# в любом из них.

# list_words = ['аквариум', 'мармелад','рама']
# list_str = ''
# for i in list_words:
#     list_str+=i
    
# dict_allin = {}

# for i in set(list_str):
#     for word in list_words:
#         if i in word:
#             if i in dict_allin.keys():
#                 dict_allin[i]+=1
#             else:
#                 dict_allin[i]=1 
                
# for item in dict_allin:
#     if dict_allin[item]==len(list_words):
#         print(item)
        
# print(dict_allin.keys())


#

# A=[[0,0,'A',0],
# [0,0,0,0],
# [0,0,0,0],
# [0,0,'B',0]]


# def recurs(A,i,j,k):
#     k+=1
#     if A[i][j]!=0 and A[i][j]!='B' and A[i][j]!='A':
#         return
#     if A[i][j]=='B':
#         return 'end '+str(k)
#     else:
#         A[i][j]=k
#         if len(A)>(i+1):
#             recurs(A,i+1,j,k)
#         if 0<=(i-1):
#             recurs(A,i-1,j,k)
#         if len(A[0])>(j+1):
#             recurs(A,i,j+1,k)
#         if 0<=(j-1):
#             recurs(A,i,j-1,k)
#         print(A)
     
# save_point = []
# for i in range(len(A)):
#     for j in range(len(A[i])):
#         if A[i][j]=='A':
#             save_point.append(i)
#             save_point.append(j)


# recurs(A,save_point[0],save_point[1],0)
            

# if len(A)>(save_point[0]+1):
#     recurs(A,save_point[0]+1,save_point[1],0)
# if 0<=(i-1):
#     recurs(A,save_point[0]-1,save_point[1],0)
# if len(A[0])>(j+1):
#     recurs(A,i,save_point[1]+1,0)
# if 0<=(j-1):
#     recurs(A,i,save_point[1]-1,0)



capsule=[1,1,1,1,1,1,1,1,1,-5,-5,-4.5,-5,-5,-5,-5,-5,1,1,1,1,1,1]

# Написать функции
# std 
# mean
# std, mean плавающие - задавать диапазон
# max,min
# Функция нормализации