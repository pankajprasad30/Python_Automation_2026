# Vd 6 : Python Variable Session1, Revision on 23/02/2026
a = 10
# a : Variable
# = : Is called assignment operator
# 10 : Value assign to the variable
# Python is dynamic programmable language that's why we are not declaring any data types.

print(a)  # 10
# id will give you the location where my value is getting stored.
print(id(a))  # 140721308959944

b = 20
print(id(b))  # 140721406936584
# Every different variable having different value will have different address.

# now lets check if two variable with have same value #
# If two variable have same value, then their address will be same.
x = 40
y = 40
print(id(x))  # 140721245718664
print(id(y))  # 140721245718664

print("X :", x, "Address: ", id(x))  # X : 40 Address:  140721308960904
print("Y :", y, "Address: ", id(y))  # Y : 40 Address:  140721308960904

############## Assign multiple value to multiple variable at a time #############
p, q, r = 10, 20, 30
print("Value of p :", p)
print("Value of q :", q)
print("Value of r :", r)
print("Value of p, q ,r : ", p, q, r)
# Value of p, q ,r :  10 20 30

############### Assign same value to multiple variable ##############
A = B = C = 100
print("Value of A :", A, (id(A)))  # Value of A : 100 140721229664264
print("Value of B :", B, (id(B)))  # Value of B : 100 140721308962824
print("Value of C :", C, (id(C)))  # Value of C : 100 140721229664264

Z = 200
# print(z) # NameError: name 'z' is not defined

############### Rules to declare variable ##############

# 1. variable name can not start with number.
var123 = 500  # correct
# 23var = 400 # wrong

# 2. variable name can not have space in between
var_name_email = 'rahul jain'  # correct
# var name = 'pankaj prasad' # wrong
# SyntaxError: invalid syntax

# 3. There is no specific length for variable name.
var_name_has_no_limit = 50
print(var_name_has_no_limit)

# 4. Python is case-sensitive. Variable name will treat differently with different case.
Name = 'Pankaj'
NAME = 'Darshika'
name = 'Neha'
namE = 'Rahul'
print(Name, NAME, name, namE)
print("\n", Name, "\n", NAME, "\n", name, "\n", namE)  # \n is used to print in next line.
# To go inside keyword Select keyword press ctrl and click.

# 5. Can not use special character in variable name.Except underscore
# var_@123 = 300 # wrong

# 6. We should not use inbuilt key word as variables.
# True = 400 # wrong
true = 900
# class = 400

################### List of keywords #######################
import keyword

print(keyword.kwlist)  # To print all list of keywords.
"""
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 
'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""
