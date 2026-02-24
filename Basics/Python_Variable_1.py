# Vd 7 : Python Variable Session2, Revision on 24/02/2026
"""
# Math Operators
+ : Plus Operator
- : Minus Operator
* : Multiplication
/ : Divide with single
// : Divide with double
% : Remainder Operator
** : Power Operator
== : Equal to operator
!= : Not equal to operator

"""

# Plus operator
n1 = 20
n2 = 34
print("Addition: ", n1+n2)
n3 = n1+n2
print("Addition of values: ", n3)

# add two strings with plus operator
var1 = "hello"
var2 = "Good Morning"
print(var1 + " " + var2)

# Can not add string with integer
v1 = 40
v2 = "Hello"
# print(v1 + v2) # wrong will give error
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

############### Subtraction ###############
a1 = 100
a2 = 90
print("Subtraction : ", a2 - a1)

############### Multiplication ###############
b1 = 30
b2 = 5
print("Multiplication : ", b1 * b2)

###### Multiply string with integer###############
# if we multiply sing with number it will repeat sting with that number of time.
c1 = "hello "
c2 = 5
print("Multiply with sting : ", c1 * c2)
# Multiply with sting :  hello hello hello hello hello

# Draw a line
print("_" * 70)
print("*" * 70)


################ Division #####################
# Division with single slash will return float value
d1 = 40
d2 = 3
print("Division with single / : ", d1/d2)
# Division with single / :  13.333333333333334

# Division with double slash will return whole number value
print("Division with single // : ", d1//d2)
# Division with single // :  13

print("_" * 70)
##################### Remainder Operator ###########################
f1 = 17
f2 = 3
print("remainder output: ", f1 % f2)

print("_" * 70)
##################### Power Operator ###########################
h1 = 5
print("Square of h1 :", h1 ** 2)
print("Qube of h1 :", h1 ** 3)

print("_" * 70)
# Solve the quadratic equation
# (a+b)^2= a^2 + b^2+ 2ab

a = 10
b = 20
lhs = (a+b)**2
rhs = a**2 + b**2 + 2*a*b
print("lhs output: ", lhs)
print("rhs output: ", rhs)
# == equal operator we will use for comparing lhs and rhs.
print(lhs == rhs)

