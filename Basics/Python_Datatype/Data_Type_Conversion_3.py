# Vd 12 : Python Data Type Conversion, Session 3, Revision on 02/03/2026

###################### Dictionary data type conversion #######################

# dict-> int : Conversion is not possible
# dict-> float : Conversion is not possible
# dict-> complex: Conversion is not possible

print("_" * 70)
# dict-> string : Conversion is possible
dict1 = {'a': 123, 'b': 231, 'c': 980}
print(dict1, type(dict1))  # {'a': 123, 'b': 231, 'c': 980} <class 'dict'>
str1 = str(dict1)
# note * indexing will start from 0, and it will consider everything like { : etc also.
print(str1, type(str1), str1[0], str1[2])  #{'a': 123, 'b': 231, 'c': 980} <class 'str'> { a


print("_" * 70)
# dict-> list : Conversion is possible
dict2 = {'a': 1233, 'b': 2321, 'c': 9820}
list2 = list(dict2) # This will give only keys, since list is single entity.
# When there is requirement ot fetch only keys then we can use this.
print(list2, type(list2)) # ['a', 'b', 'c'] <class 'list'>

print(dict2.items()) # dict_items([('a', 1233), ('b', 2321), ('c', 9820)])

print("_" * 70)
# dict-> tuple : Conversion is possible
dict3 = {'a': 1233, 'b': 2321, 'c': 9820}
tup3 = tuple(dict3)
print(tup3, type(tup3)) # ('a', 'b', 'c') <class 'tuple'>

print("_" * 70)
# dict-> set : Conversion is possible
dict4 = {'a': 1233, 'b': 2321, 'c': 9820}
set4 = set(dict4)
print(set4, type(set4)) # {'c', 'b', 'a'} <class 'set'>

print("_" * 70)
# dict-> boolean : Conversion is possible
# when value is empty it will give false
dict5 = {}
bool5 = bool(dict5)
print(bool5, type(bool5)) #False <class 'bool'>

# When we have some value it will give true
dict6 = {'a': 1233, 'b': 2321}
bool6 = bool(dict6)
print(bool6, type(bool6)) #True <class 'bool'>

print("_" * 70)
############################# Set data type conversion ####################################

# set-> int : conversion is not possible
# set-> float : conversion is not possible
# set-> complex : conversion is not possible

# set-> string : conversion is possible
set1 = {3, 4, 5, 'a', 7, 80}  # it will pic ramdom value.
string_a = str(set1)
print(string_a, type(string_a), string_a[1], string_a[2])  #{80, 3, 4, 5, 7} <class 'str'> 8 0

print("_" * 70)
# set-> list : conversion is possible

set2 = {3, 4, 5, 'a', 7, 80, 60, 22, 11}
list_a = list(set2)
print(list_a, type(list_a)) # [3, 4, 5, 7, 'a', 11, 80, 22, 60] <class 'list'>
print(list_a[0], list_a[2])

print("_" * 70)
# set-> tuple : conversion is possible
set3 = {3, 4, 5, 'a', 7, 80, 60, 22, 11}
tup_a = tuple(set3)
print(tup_a, type(tup_a)) # (3, 4, 5, 7, 11, 80, 'a', 22, 60) <class 'tuple'>

print("_" * 70)
# set-> dict : conversion is possible
set4 = {3, 4, 5, 'a', 7, 80, 60, 22, 11}
#dict_a = dict(set4)
# print(dict_a) # TypeError: cannot convert dictionary update sequence element #0 to a sequence

print("_" * 70)
# set-> boolean : conversion is possible
set5 = {3, 4, 5, 'a', 7, 80, 60, 22, 11}
bool_a = bool(set5)
print(bool_a, type(bool_a)) # True <class 'bool'>

set6 = {}
bool_b = bool(set6)
print(bool_b, type(bool_b))  # False <class 'bool'>

print("_" * 70)
############################# Boolean data type conversion ####################################

# boolean -> int  : conversion is possible
b1 = True
n1 = int(b1)
print(n1, type(n1)) # 1 <class 'int'> : For True

b2 = False
n2 = int(b2)
print(n2, type(n2)) # 0 <class 'int'> : For False

# boolean -> float  : conversion is possible
b3 = True
n3 = float(b3)
print(n3, type(n3))  # 1.0 <class 'float'>

b4 = False
n4 = float(b4)
print(n4, type(n4)) # 0.0 <class 'float'>

# boolean -> complex  : conversion is possible
b5 = False
n5 = complex(b5)
print(n5, type(n5))  # 0j <class 'complex'>
# For True : op is --> (1+0j) <class 'complex'>


# boolean -> string  : conversion is possible
b6 = False
n6 = str(b6)
print(n6, type(n6), n6[0])  # False <class 'str'> F

# boolean -> list  : conversion is not possible, it's not iterable
# boolean -> tuple  : conversion is not possible.
# boolean -> dict  : conversion is not possible.
# boolean -> set  : conversion is not possible.

