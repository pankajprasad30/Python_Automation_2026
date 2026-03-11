# Vd 14 : Python nested-if basics, Session 1, Revision on 11/03/2026

print("_" * 70)
"""
if cond1: 
    code
    if cond2:
        code
        if cond3:
            code
        else:
            code
    else:
        code           
else:
    code

"""

# WAP to simulate the interview process with the help of nested if condition.
round1 = 'pass'
round2 = 'pass'
round3 = 'pass'

if round1 == "pass":
    print("Congrats 1st round is clear")

    if round2 == "pass":
        print("Congrats 2nd round is clear")

        if round3 == "pass":
            print("Congrats you are selected")
        else:
            print("Failed in last round, please try next time")
    else:
        print("Failed in 2nd round, Try next time")

else:
    print("Failed in 1st round, Try next time")

# WAP to check given number is positive or negative
num1 = 50

if num1 > 0:
    print(num1 ** 3)
    if num1 > 10 and num1 < 20:
        print(num1 // 2)
    elif num1 > 20 and num1 < 30:
        print(num1 // 4)
    else:
        print(num1 // 5)
else:
    print(num1 ** 2)
    if num1 > -10 and num1 < -50:
        print(num1 * 2)
    elif num1 > - 50 and num1 < -100:
        print(num1 * 4)
    else:
        print(num1 * 5)

print("_" * 70)
# write a prog in one single line
# check for odd and even

num2 = 51
# Note : if writing code in single line then colon: is not require, also indentation not required.
result = "Even" if num2 % 2 == 0 else "Odd"
print("Output:", result)

# WAP to check if any person can vote or not
age = 18
result = "He can vote" if age >= 18 else "He can't vote"
print("Output", result)

print("_" * 70)
# WAP to calculate the bill amount on the basis of unit consumption.
units = 100
total_bill = 0
if units <= 100:
    #total_bill = total_bill + units * 15
    total_bill += units * 15
    #total_bill = units * 15
elif 100 < units <= 200:
    total_bill = total_bill + units * 18
elif 200 < units <= 300:
    total_bill = total_bill + units * 20
else:
    total_bill = total_bill + units * 25

print("Total Bill Amount: ", total_bill)

# Check any given number is in list or not.
val = 5
list1 = [50, 3, 30, 90, 10, 11]

result = True if val in list1 else False
print("Result: ", result)
# or
if val in list1:
    print("Value is available in the list:", val, list1)
else:
    print("Value is not available in the list:", val, list1)

# check is any character is available in the string.
string1 = "Hello"
char = 'd'
if char in string1:
    print("Character is available in string : ", char)
else:
    print("Character is not available in string: ", char)

