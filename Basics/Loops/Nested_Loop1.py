# Vd 17 : Python nested-loop practise, Session 2, Revision on 18/03/2026

# WAP to print below pattern
"""
* * * * *
* * * *
* * *
* *
*
"""

print("_" * 70)
# WAP with single for loop for above pattern.
for i in range(6, 0, -1):
    print(" * " * i)

print("_" * 70)
# WAP with nested for loop for above pattern.
for i in range(6, 1, -1):
    for j in range(1, i):
        print(" * ", end=" ")
    print()

print("_" * 70)
# Prime number: number which is divisible by 1 or itself
# WAP to check given number is Prime or not.

num = 7
count = 0
for i in range(2, num // 2):
    if num % i == 0:
        count += 1
        # count = count + 1
print("Count value :", count)
if count == 0:
    print("This number is prime number: ", num)
else:
    print("This number is not prime number: ", num)

# Another way
print("_" * 70)
num = 9
prime = True

for i in range(2, num // 2):
    if num % i == 0:
        prime = False

if prime:
    print("This number is prime number: ", num)
else:
    print("This number is not prime number: ", num)

print("_" * 70)
# WAP to get list of prime numbers from 1 to 100.

prime_list = []
for i in range(2, 101):
    prime = True
    for k in range(2, i):
        if i % k == 0:
            prime = False
    if prime:
        print(i, end=" ")
        prime_list.append(i)
print()
print(prime_list)

print("_" * 70)
"""
# # @ # #
# @ # @ #
@ # # # @
# @ # @ #
# # @ # #
"""
# first create structure of 5 X 5
for i in range(1, 6):
    for j in range(1, 6):
        if i == 1 and j == 3:
            print("@", end=" ")
        elif (i == 2 and j == 2) or (i == 2 and j == 4):
            print("@", end=" ")
        elif (i == 3 and j == 1) or (i == 3 and j == 5):
            print("@", end=" ")
        elif (i == 4 and j == 2) or (i == 4 and j == 4):
            print("@", end=" ")
        elif i == 5 and j == 3:
            print("@", end=" ")

        else:
            print(" ", end=" ")

    print()

print("_" * 70)
"""
# # @ # #
# @ @ @ #
@ @ @ @ @
# @ @ @ #
# # @ # #
"""

num_star = 5
num_rows = 5
a = 2
b = 4

for i in range(1, num_rows + 1):
    if i >= 4:
        a = a + 2
        b = b - 2
    for j in range(1, num_star + 1):
        if j > a and j < b:
            print("@", end=" ")
        else:
            print("#", end=" ")
    if i <= 4:
        a = a - 1
        b = b + 1

    print()
