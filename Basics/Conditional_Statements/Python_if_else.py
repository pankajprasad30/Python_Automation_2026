# Vd 12 : Python if-else basics, Session 1, Revision on 02/03/2026

"""
if condition:
   code
else:
   code
"""

print("_" * 70)
# compare two number, weather equal or not.
a = 40
b = 40
# maintain intention

print('Condition output: ', a == b)

if a == b:
    # if condition is true
    print("Numbers are equal")
else:
    # if condition is false
    print("Numbers are not equal")


print("_" * 70)
# WAP to check given number is even or odd.
# if any number is divisible by 2 then it's even else odd.

#num1 = 7
num1 = int(input("Please input any number: "))
# For human input
# and since input number is in string, so we are converting into integer.
if num1 % 2 == 0:
    print("It is even number")
else:
    print("It is odd number")


