# fl = int(input())
# tic = int(input())
 
# res = tic%fl

# if res==0:
#     print(fl)
# else:
#     print(res)
    
x = int(input())
y = int(input())
z = int(input())
#Решение долгое
# steps = 0
# while(True):
#     if x==0:
#         break
#     else:
#         steps+=1
#         x-=1
#     if y==0:
#         break
#     else:
#         steps+=1
#         y-=1
#     if z==0:
#         break
#     else:
#         z-=1
#         steps+=1

#     if y==0:
#         break
#     else:
#         y-=1
#         steps+=1
# print(steps)
    
k = min(x,y//2,z)
x-=k
z-=k
y-=2*k

if x==0:
    print(k*4)
else:
    if y==0:
        print(k*4+1)
    else:
        if z==0:
            print(k*4+2)
