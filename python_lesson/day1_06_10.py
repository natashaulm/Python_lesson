# import pandas
# import datatable
#
# import numpy
# import matplotlib
#
# import statsmodels
#
# mas=[1,2,3,4,5,6,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,9,10]
#
#
# x = 8
# count1 = 0
# for i in mas:
#     count1+=1
#     if i == 8:
#         print(count1)
#         break
#
# # n
# count2 = 0
#
#
# first = 0
# last = len(mas)
# medium=len(mas)//2
#
# while mas[medium] != x and first<=last:
#     count2+=1
#     print(medium)
#     if x>mas[medium]:
#         first=medium+1
#     else:
#         last=medium-1
#     medium=(first+last)//2
#
# if first>last:
#     print('nothing')
# else:
#     print(medium,count2)


def factor(number: int) -> int:
    if number == 1:
        return 1
    else:
        return factor(number-1)*number

# factor(5)

def new_sum(newlist: list[int]):
    sum = 0
    for i in newlist:
        sum+=i
    print(sum)

new_sum([1,2,3,4,5])
