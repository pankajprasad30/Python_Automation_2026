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
