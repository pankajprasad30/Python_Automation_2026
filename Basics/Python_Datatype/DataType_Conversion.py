# Vd 10 : Python Data Type Conversion Session 1, Revision on 26/02/2026

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

print("_" * 70)
############################## Int #####################################

# int -> float
n1 = 55
f1 = float(n1)
print(f1, type(f1))

# int -> string
n2 = 40414134234
s1 = str(n2)
print(s1, type(s1))
print(s1[2])  # since its string now so it should follow properties of string.

print("_" * 70)
# int -> list : Conversion is not possible
n3 = 4234
# l1 = list(n3)
# print(n3, type(l1)) # TypeError: 'int' object is not iterable

# int -> tuple : Conversion is not possible
# int -> dict : Conversion is not possible
# int -> set : Conversion is not possible

print("_" * 70)
# int -> complex (Real & Imaginary) :
n4 = 200
c1 = complex(n4)
print(c1, type(c1))  # (200+0j) <class 'complex'>
# Default imaginary value will be zero.

print("_" * 70)
# int -> boolean (Real & Imaginary) :
a5 = 0
b2 = bool(a5)
print(b2, type(b2)) # False <class 'bool'>

a6 = 3
b3 = bool(a6)
print(b3, type(b3)) # True <class 'bool'

print("_" * 70)
############################## Float Data Type ##############################
# float-> int
fl2 = 33.33
in1 = int(fl2)
print(in1, type(in1)) # 33 <class 'int'>

# float-> string
fl3 = 33.45
str1 = str(fl3)
print(str1, type(str1), str1[-2]) #33.45 <class 'str'> 4

# time : 48:49

# float-> complex
fl4 = 44.4
com1 = complex(fl4)
print(com1, type(com1)) # (44.4+0j) <class 'complex'>

# float-> list --> Conversion is not possible.
# float-> tuple --> Conversion is not possible.
# float-> dict --> Conversion is not possible.
# float-> set --> Conversion is not possible.

# float-> boolean
fl5 = 44.4
bool1 = bool(fl4)
print(bool1, type(bool1)) # True <class 'bool'>

fl6 = 0.000
bool2 = bool(fl6)
print(bool2, type(bool2)) # False <class 'bool'>

print("_" * 70)
############################## String Data Type ##############################

# String-> int
str1 = 'Hello'
#num1 = int(str1)
#print(num1) # ValueError: invalid literal for int() with base 10: 'Hello'

#Note* if string only contains number then conversion is possible.
str2 = 123
num2 = int(str2)
print(num2, type(num2), num2 * 10) # 123 <class 'int'> 1230

# String-> float
# Note* : if string contains only pointer value then conversion is possible.
str3 = 44.3
num3 = float(str3)
print(num3, type(num3), num3 * 10) #44.3 <class 'float'> 443.0

print("_" * 70)
# String-> complex
str5 = '50+60j'
com5 = complex(str5)
print(com5, type(com5), com5.real, com5.imag) #(50+60j) <class 'complex'> 50.0 60.0

print("_" * 70)
# String-> list
str_a = "Python"
list_a = list(str_a)
print(list_a, type(list_a)) # ['P', 'y', 't', 'h', 'o', 'n'] <class 'list'>
