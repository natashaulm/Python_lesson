# import string
#
# message = 'Hello, world, !!!!,caps,Hello,llll'.lower()
#
# for char in string.punctuation:
#     if char in message:
#         message = message.replace(char, ' ')
#
# dict_log = dict()
# for i in set(message.split()):
#     dict_log[i]=message.split().count(i)
#
# print(dict_log)

# def pair_match(lst1: list, lst2: list):
#     n = min(len(lst1), len(lst2))
#     lst3 = []
#     for i in range(n):
#         lst3.append((lst1[i],lst2[i]))
#     return lst3
#
# lst1=[1,2,3]
# lst2=['a','b','c','d']
#
# result = pair_match(lst1,lst2)
# print(result)
#
# def unique_value(lst1: list):
#     return set(lst1)
#
# lst1 = [1,1,1,1,1,1,1,2,2,2,2,3,4,5,6,3,2,4]
# print(unique_value(lst1))
#
# def unique_value2(lst1: list):
#     list_data = []
#     for i in lst1:
#         if i not in list_data:
#             list_data.append(i)
#     return list_data
#
# lst2 = [1,1,1,1,1,1,1,2,2,2,2,3,4,5,6,3,2,4]
# print(unique_value2(lst2))


# def combine_dicts(dict1:dict,dict2:dict):
#     for i in dict2.keys():
#         if i in dict1.keys():
#             dict1[i]+=dict2[i]
#         else:
#             dict1[i] = dict2[i]
#     return dict1
#
# dict1 = {'a':1,'b':2}
# dict2 = {'b':3,'c':4}
# result = combine_dicts(dict1,dict2)
# print(result)

# def reverse_tuples(tuples: list):
#     new_list = []
#     for i in range(len(tuples)):
#         new_list.append((tuples[i][1],tuples[i][0]))
#     return new_list
#
# tuples = [(1, 2), (3, 4), (5, 6)]
# result = reverse_tuples(tuples)
# print(result)


# import copy
#
# mas=[1,2,3,4]
#
# type_mas = mas
# type_mas2 = copy.deepcopy(mas)
# print(type_mas)
# print(type_mas2)
#
# mas[0]=11
#
# print(type_mas)
# print(type_mas2)


# def upper_mas(lst:list):
#     lst2=lst
#     for i in range(len(lst2)):
#         lst2[i]= 1 if i%2==0 else 0
#
# mas=[1,2,3,4,5]
# upper_mas(mas)
# print(mas)


# [1, 0, 0, 0, 0, 0, 0, 0],
# [#, 1, 0, 0, 0, 0, 0, 0],
# [#, #, 1, 0, 0, 0, 0, 0],
# [#, #, #, 1, 0, 0, 0, 0],
# [#, #, #, #, 1, 0, 0, 0],
# [#, #, #, #, #, 1, 0, 0],
# [#, #, #, #, #, #, 1, 0],
# [#, #, #, #, #, #, #, 1]


# def fibon(n:int)-> int:
#   if n < 2:
#     return n
#   else:
#     return fibon(n-1) + fibon(n-2)
#
# A=[[1, 0, 0, 0, 0, 0, 0, 0],
# [fibon(1), 1, 0, 0, 0, 0, 0, 0],
# [fibon(1), fibon(1), 1, 0, 0, 0, 0, 0],
# [fibon(1), fibon(1), fibon(1), 1, 0, 0, 0, 0],
# [fibon(1), fibon(1), fibon(1), fibon(1), 1, 0, 0, 0],
# [fibon(1), fibon(1), fibon(1), fibon(1), fibon(1), 1, 0, 0],
# [fibon(1), fibon(1), fibon(1), fibon(1), fibon(1), fibon(1), 1, 0],
# [fibon(1), fibon(1), fibon(1), fibon(1), fibon(1), fibon(1), fibon(1), 1]]
# n=8
# sum=0
# for i in range(1,8):
#     for j in range(i):
#         sum+=A[i][j]
# print(sum)


