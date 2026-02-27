# Vd 11 : Python Data Type Conversion, Session 2, Revision on 27/02/2026

print("_" * 70)
# String-> tuple
str_a = "Good Morning"
tup_a = tuple(str_a)
print(tup_a, type(tup_a), str_a[3])
# ('G', 'o', 'o', 'd', ' ', 'M', 'o', 'r', 'n', 'i', 'n', 'g') <class 'tuple'> d

print("_" * 70)
# String-> dict
# Conversion is not possible, ValueError: dictionary update sequence element #0 has length 1; 2 is required
# str_b = "Good Evening"
# dict_a = dict(str_b)
# print(dict_a)

# What if string follows the properties of dict, lets see with below code
# If string follow the dict rules and pattern then string to dict conversion is possible with the
# help of json module.
import json

str_c = '{"a": 123, "b": 3423, "c": 9879}'  # double quote will work since it follows json pattern.
# str_c = "{'a': 123, 'b': 3423, 'c': 9879}"
# dict_b = dict(str_c)
print(str_c, type(str_c))

result = json.loads(str_c)
print(result, type(result))  # {'a': 123, 'b': 3423, 'c': 9879} <class 'dict'>
print(result["b"])

print("_" * 70)
# String-> set
str_d = "Good Morning"
set_a = set(str_d)
print(set_a, type(set_a))  # {'o', 'M', 'g', 'd', ' ', 'r', 'n', 'i', 'G'}
# note*:  duplicate values are removed

print("_" * 70)
# String-> boolean
str_e = ""  # for empty will give false
bool_a = bool(str_e)
print(bool_a, type(bool_a))  # False <class 'bool'>

str_f = "Hello"  # for some value it will give true , even for space also
bool_b = bool(str_f)
print(bool_b, type(bool_b))  # True <class 'bool'>

#################################### List data type conversion ##############################

print("_" * 70)
# list-> int:  conversion is not possible
# list-> float : conversion is not possible
# list-> complex: conversion is not possible

# list-> string: conversion is possible
list1 = [2, 5, 7, 8, 9] # indexing will start from bracket
str1 = str(list1)
print(str1, type(str1))
print(str1[0], str1[1], str1[4], str1[10])  # [ 2 5 8

print("_" * 70)
# list-> tuple:

list2 = ['a', 2.5, [5, 7, 8], (9, 7)]
tup1 = tuple(list2)
print(tup1, type(tup1)) # ('a', 2.5, [5, 7, 8], (9, 7)) <class 'tuple'>
print(tup1[-1]) #(9, 7)

print("_" * 70)
# list-> dict:

# direct conversion is not possible
#list3 = [3, 4, 6, 9, 10]
#dict1 = dict(list3)
#print(dict1, type(dict1))
# TypeError: cannot convert dictionary update sequence element #0 to a sequence

# if we have two list and wants to convert in dict then we can use zip function
list4 = ['a', 'b', 'c', 'd', 'e']
list5 = [3, 4, 6, 9, 10, 90] # extra value of 90 is ignored
result = dict(zip(list4, list5))
print(result, type(result))  # {'a': 3, 'b': 4, 'c': 6, 'd': 9, 'e': 10} <class 'dict'>
print(result['d'])  # 9

list_a = ('a', 'b', 'c', 'd', 'e') # tuple
list_b = (3, 4, 6, 9, 10, 90)
result2 = dict(zip(list_a, list_b))
print(result2)  # {'a': 3, 'b': 4, 'c': 6, 'd': 9, 'e': 10}

print("_" * 70)
# list -> set
list_1 = [4, 5, 7, 90, 3, 4, 90]
set_1 = set(list_1)
print(set_1, type(set_1)) # {3, 4, 5, 7, 90} <class 'set'>

print("_" * 70)
# list -> boolean
list_2 = []
bool_2 = bool(list_2)
print(bool_2, type(bool_2)) #False <class 'bool'>

list_3 = [2]
bool_3 = bool(list_3)
print(bool_3, type(bool_3)) # True <class 'bool'>

######################## Tuple data type ###################################

# Tup -> int : Conversion is not possible
# Tup -> float : Conversion is not possible
# Tup -> complex : Conversion is not possible

# Tup -> string : Conversion is possible
tup_a = (5, 7, 90, 1)
str_a = str(tup_a)
print(str_a, type(str_a), str_a[0]) # (5, 7, 90, 1) <class 'str'> (

# tup-> list
tup_b = (5, 7, 90, 1)
list_b = list(tup_b)
print(list_b, type(list_b), list_b[0]) # [5, 7, 90, 1] <class 'list'> 5

# Tup -> dict : Conversion is not possible
# only we can convert to tuple using zip function.

tup_4 = ('a', 'b', 'c', 'd', 'e')
tup_5 = (3, 4, 6, 9, 10, 90) # extra value of 90 is ignored
result = dict(zip(tup_4, tup_5))
print(result) # {'a': 3, 'b': 4, 'c': 6, 'd': 9, 'e': 10}

# Tup -> set :

tup_q = (3, 4, 6, 9, 10, 90)
set_q = set(tup_q)
print(set_q, type(set_q))  # {3, 4, 6, 9, 10, 90} <class 'set'>

print("_" * 70)
# Tup -> boolean
tup_w = tuple() # for empty adding tuple before bracket
b1 = bool(tup_w)
print(b1, type(b1)) # False <class 'bool'>

tup_r = (2, 5, 9, 10, 33, 44)
b2 = bool(tup_r)
print(b2, type(b2)) # True <class 'bool'>




