# Vd 8 : Python Data Type Session 1, Revision on 25/02/2026
"""
Python Datatypes:
1. Number
   a) Integer : Immutable
   b) Float : Immutable
   c) Complex : Immutable
2. Sequential
   a) String : Immutable
   b) List : Mutable
   c) Tuple : Immutable
3. Dictionary : : Mutable
4. Set : Mutable
5. Boolean : Mutable

"""
###################### Integer Data Type ######################
n1 = 30  # any whole number
print(n1, type(n1))  # 30 <class 'int'>

"""
Basic properties of integer data types:-
1. Integer is a immutable data type, once it's defined it can not changed.
2. There is no limit for integer data type.
3. Integer always consider the whole numer.
4. integer always consider +ve and -ve whole number.
"""

n2 = 14124124124
print(n2, type(n2))  # 14124124124 <class 'int'>

n3 = 0
print(n3, type(n3))  # 0 <class 'int'>

n4 = -114124
print(n4, type(n4))
# when we add two integer value then output will be integer only
v1 = 100
v2 = 300
v3 = v1 + v2
print(v3, type(v3))  # 400 <class 'int'>

# l1 = [2, 4, 5]
# l1.append(30)
# print(l1)

i1 = int()  # initializing i1 without any value
print(i1)  # Default value of int is 0

print("_" * 70)
###################### Float Data Type ######################

f1 = 30.3
print(f1, type(f1))  # 30.3 <class 'float'>

"""
Properties of float:-
1. Float is a immutable data type.
2. There is no specific limit for float data type.
3. All the pointer values will be consider as float. (Both +ve and -ve)

"""
v1 = 30.3 + 55.6
print(v1, type(v1))

v2 = 0.0
print(v2, type(v2))
v3 = 0.43432423423
print(v3, type(v3))
v4 = 11.1141
print(v4, type(v4))
v5 = 3242315125523521.23523523
print(v5, type(v5))

print("_" * 70)
###################### Complex Data Type ######################

# Complex number represent with x+yj
q1 = 10 + 20j
print(q1, type(q1))  # (10+20j) <class 'complex'>

q2 = 2.3 + 44.3j
print(q2, type(q2))

result = q1 + q2
print(result, type(result))  # (12.3+64.3j) <class 'complex'>

# Complex number
q4 = q1 * 2
print(q4, type(q4))  # (20+40j) <class 'complex'>

q5 = 44 + 75j
print("Real number: ", q5.real)
print("Imaginary number : ", q5.imag)

print("_" * 70)
###################### String Data Type ######################

"""
# Properties
1. String is immutable data type
2. Anything with single double and triple quote will consider as string.
3. String follows +ve & -ve indexing.
4. String is sequential data type
5. String can contain any type of data, int, flot, str, special character.
6. 

"""

s1 = " Hello"
print(s1, type(s1))  # Hello <class 'str'>
s = str()
print(s, type(s))
s0 = ' '
print(s0, type(s0))
s2 = " "
print(s2, type(s2))
s3 = 'A'
print(s3, type(s3))
s4 = "B"
print(s4, type(s4))
s5 = 'Python'
print(s5, type(s5))
s6 = "Hello i am revising Python"
print(s6, type(s6))
s7 = """Pankaj Prasad"""
print(s7, type(s7))
s8 = "Hello 'good' morning1112214343"
print(s8, type(s8))
s9 = 'Hello good evening, enjoy "today" party'
print(s9, type(s9))

# If you want to print output in multiline then put under triple quote
s10 = """ Hello we are learning python.
Python programming 'and' learning is fun.
Its easy "to" understand
"""
# String concatenation
var1 = "Nice"
s11 = "Have a " + var1 + " day"
print(s11, type(s11))

print("_" * 70)
s12 = "3123 .45 [5, 4, 3.6]%@$(!@%"
print(s12, type(s12))

# Vd 9 : Python Data Type Session 2, Revision on 25/02/2026

# Indexing of string (It follows indexing that's why it's called sequential data type)
print("_" * 70)
str_1 = "Python"

"""
0 1 2 3 4 5 +ve indexing
P y t h o n
-6 -5 -4 -3 -2 -1 -ve indexing
"""

print(str_1[0])  # P
print(str_1[-1])  # n
print(str_1[-3])  # h

length = len(str_1)
print("Length of string: ", length)

print(str_1.index('P'))  # index
print(str_1[2:4])  # slicing

print("_" * 70)
###################### String Data Type ######################
# list is combination of all data types
list1 = [2, 3.3, 23123, 'Hello', True]
print(list1, type(list1))

"""
# Properties of list data type
1. List is a mutable data type, we can modify any point of time.
2. List follows +ve and -ve indexing.
3. List can contain all different data type, int , string, float, dictionary, set, tuple etc
4. We define the list with square bracket.
"""

#        0    1   2   3         4
list2 = [33, 44, 55, [2, 3.3], 'Hello']
#       -5   -4  -3  -2        -1
list2.append(100)
print(list2)  # [33, 44, 55, [2, 3.3], 'Hello', 100]

# Anything starting with def is a function.

print(dir(list))  # this will give list of all methods for particular data types.
"""
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', 
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', 
'__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', 
'__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', 
'__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 
'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# __ are called magic functions, python use it for internal purpose.

We are going to use these list of method :
'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

"""
print(dir(str))

# what is the difference between method and function ?
# Method : it's a member of particular class.
# Function: it's individual entity.

# Print Hello from the list.
#        0    1   2   3         4
list3 = [33, 44, 55, [2, 3.3], 'Hello']
#       -5   -4  -3  -2        -1

print(list3[4])
print(list3[-2])  # [2, 3.3] its called as child list
print(list3[2:5])
print(list3[2:9])

print(list3[1], list3[4])

var4 = 'Name'
var5 = 'age'
var6 = 300
list4 = [var4, var5, var6]
print(list4, type(list4))
#                     Dictionary: Store value in key value format
list10 = [(2, 4, 5), {'a': 123, 'b': 323}, {2, 4, 5}]
print(list10, type(list10))
print(list10[0])  # (2, 4, 5)
print(list10[1])  # {'a': 123, 'b': 323}
print(list10[2])  # {2, 4, 5}

# set store unique data type


print("_" * 70)
###################### Tuple Data Type ######################

# Here data will not modify
tup1 = (2, 3, 5, 'Hello', 3.5, [3, 4, 5], (3, 6, 6.7))
print(tup1, type(tup1))  # (2, 3, 5, 'Hello', 3.5, [3, 4, 5], (3, 6, 6.7)) <class 'tuple'>

"""
# Properties of tuple
1. Tuple is a immutable data type, once it is defined we can not change it.
2. Tuple can contain all different type of data, int float, list, tuple dict, set, boolean
3. Tuple follows indexing positive and negative.
4. Tuple defined with round bracket.
"""
#      0   1  2   3       4     5          6
tup2 = (2, 3, 5, 'Hello', 3.5, [3, 4, 5], (3, 6, 6.7))
#       -6   -5   -4      -3    -2         -1

# dir : dir return list of method belongs to specific class
print(dir(tuple))  # 'count', 'index'

print(tup2[5])  # [3, 4, 5]
print(tup2.count(3))

length_tup = len(tup2)
print("Length of tuple: ", length_tup)

# Empty tuple
tup3 = tuple()
print(tup3, type(tup3))

print("_" * 70)
###################### Dictionary Data Type ######################

dict1 = {'a': 212, 'b': 131, 'c': 989}
print(dict1, type(dict1))  # {'a': 212, 'b': 131, 'c': 989} <class 'dict'>

"""
# properties of dictionary:-
1. Dictionary is mutable data type, we can modify and update.
2. Dictionary only contains unique key, duplicate keys are not allowed.
3. it store data in key value format.
4. It only contains immutable data type as key. int, float, string, tuple. boolean
5. list, dict and set can be the key in dictionary.
6. it can contain all different dat type as value.
7. for dict value no restriction, it can contain all types of data. int float string list tuple dict boolean set.
8. it does not follow any indexing.
9. it follows LIFO (Last In First Out)
"""

dict2 = {'Name': "Pankaj", 'Age': 39, 'City': "Bangalore", 'EMail': "pankajprasad30@gmail.com"}
# get value from dict by using key
print(dict2['EMail'])

# add data into dict (It will add data at end)
dict2['Phone no'] = 9931231233
print(dict2)
# this will remove data which is last inserted.
dict2.popitem()
print(dict2)

dict2.pop('City')
print(dict2)

var10 = 700
var11 = {'emp_name': 'pankaj', 'emp_Salary': 700000}
dict3 = {
    123: 3.5,
    3.5: 'Hello',
    'Python': [2, 3, 4],
    # [1, 2, 3]: (2, 5, 7) # TypeError: unhashable type: 'list'
    (2, 5, 9): {'a': 123, 'b': 300},
    # 123 : 300 # if same key is defined then it will override on previous key value
    var10: "Prgogramming",
    'employee_details': var11

}
# print(dict3)

# By below method will get in structure format output.
from pprint import pprint

pprint(dict3)
# how to fetch name
print("_" * 70)
dict4 = {
    123: 3.5,
    3.5: 'Hello',
    'Python': [2, 3, 4],
    (2, 5, 9): {'a': 123, 'b': 300},
    var10: "Prgogramming",
    'employee_details': {'designation': 'Software Tester',
                         'emp_name': 'pankaj',
                         'emp_Salary': 700000}

}
print(dict4['employee_details']['emp_name'])
