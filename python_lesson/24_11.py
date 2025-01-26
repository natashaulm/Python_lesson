# n = int(input())
# k = int(input())

# print((2*n*(n//k-1)))

N = int(input())

list_winner = {1:{'id':[],'time_m':60,'time_s':60},
               2:{'id':[],'time_m':60,'time_s':60},
               3:{'id':[],'time_m':60,'time_s':60}}
for i in range(N):
    stroka =  input().split()
    id = int(stroka[0])
    split_time = stroka[1].split(':')
    time = [int(split_time[0]),int(split_time[1])] 
    for j in list_winner:
        if (list_winner[j]['time_m']>time[0]) or \
        (list_winner[j]['time_m']==time[0] and \
        list_winner[j]['time_s']>time[1]):
            for k in range(3,j,-1):
                list_winner[k]=list_winner[k-1].copy()
            list_winner[j]['id']=[id]
            list_winner[j]['time_m']=time[0]
            list_winner[j]['time_s']=time[1]
            break
        elif list_winner[j]['time_m']==time[0] and list_winner[j]['time_s']==time[1]:
            list_winner[j]['id'].append(id)
            break

for i in list_winner:
    print(list_winner[i]['id'])     
        
        






# print('x,y,z,w')

# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not(((x or not(y)) and (not(z)==w))<=(y and z)):
#                     print(x,y,z,w)




# def troy(N):
#     Rtr = ''
#     while N>0:
#         Rtr = str(N%3) + Rtr
#         N//=3
#     return Rtr


# def f(N):
#     R = troy(N)
#     if N%3 == 0:
#         R += R[-3:]
#     else:
#         Param = (N%3)*3
#         R += troy(Param) 
#     R = int(R,3)
#     return R
    
    

# for i in range(1,1000):
#     if f(i)>150:
#         print(i)
#         break
        
    
            


# from itertools import permutations
# stroka = '0123456789'
# count=0
# for i in permutations(stroka,4):
#     if i[0] != '0' and (int(i[0])%2 != int(i[1])%2) and (int(i[1])%2 != int(i[2])%2) and (int(i[2])%2 != int(i[3])%2):
#        count+=1

# print(count) 


# from itertools import product
# letters = 'ABCDXYZ'
# count=0
# for i in product(letters,repeat=4):
#     slovo = ''.join(i)
#     if (slovo[0] in 'XYZ' and (slovo.count('Y')+slovo.count('X')+slovo.count('Z'))==1): 
#         count+=1
    
# print(count)
    



# from itertools import product
# letters = 'АОУ'
# count=0
# for i in product(letters,repeat=5):
#     count+=1
#     if ''.join(i)=='УАУАУ':
#         print(count)
#         break
    
    
    