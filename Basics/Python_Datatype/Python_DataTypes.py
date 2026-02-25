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
n1 = 30 # any whole number
print(n1, type(n1)) # 30 <class 'int'>

"""
Basic properties of integer data types:-
1. Integer is a immutable data type, once it's defined it can not changed.
2. There is no limit for integer data type.
3. Integer always consider the whole numer.
4. integer always consider +ve and -ve whole number.
"""

n2 = 14124124124
print(n2, type(n2)) # 14124124124 <class 'int'>

n3 = 0
print(n3, type(n3)) # 0 <class 'int'>

n4 = -114124
print(n4, type(n4))
# when we add two integer value then output will be integer only
v1 = 100
v2 = 300
v3 = v1 + v2
print(v3, type(v3)) # 400 <class 'int'>

# l1 = [2, 4, 5]
# l1.append(30)
# print(l1)

i1 = int() # initializing i1 without any value
print(i1) # Default value of int is 0

print("_" * 70)
###################### Float Data Type ######################

f1 = 30.3
print(f1, type(f1)) # 30.3 <class 'float'>

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
print(q1, type(q1)) #(10+20j) <class 'complex'>

q2 = 2.3 + 44.3j
print(q2, type(q2))

result = q1 + q2
print(result, type(result)) #(12.3+64.3j) <class 'complex'>

# Complex number
q4 = q1 * 2
print(q4, type(q4)) # (20+40j) <class 'complex'>

q5 = 44 + 75j
print("Real number: ", q5.real)
print("Imaginary number : ", q5.imag)

print("_" * 70)
###################### String Data Type ######################

s1 = " Hello"
print(s1, type(s1))# Hello <class 'str'>
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
s11 = "Have a "+var1+" day"
print(s11, type(s11))