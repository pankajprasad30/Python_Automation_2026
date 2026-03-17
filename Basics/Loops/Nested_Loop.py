# Vd 16 : Python nested-loop basics, Session 1, Revision on 17/03/2026
"""
# Means loop inside loop
for cond1:
    code
    for cond2:
        code

"""
"""
# Outer loop
for i in range(1, 5):  # i =1 (for one single outer loop 3 time inner loop execute)
    # Inner loop
    print(("Address: ", i))  # j=1, 2, 3
    for j in range(1, 4):
        print("Package: ", j)
    print("_" * 70)

# multiple ineer loop
for a in range(1, 5):
    print("Address:", a)
    for b in range(1, 4):
        print("Package", b)
    for c in ['Hello', 'Good', 'Morning']:
        print('Greetings', c)
    print("_" * 70)
    
"""

# Multi level inner loop
# Outer loop -> inner loop -> inner loop
"""
for a in range(1, 5):
    print("Address:", a)
    for b in range(1, 4):
        print("Package", b)
        for c in ['Hello', 'Good', 'Morning']:
            print('Greetings', c)

    print("_" * 70)

"""

############################ Execute inner loop with condition #################################

for a in range(1, 5):
    print("Address:", a)
    # Inner loop 1
    for b in range(1, 4):
        print("Package", b)
        # Inner loop 2
        if a == 1 or a == 4:
            for c in ['Hello', 'Good', 'Morning']:
                print('Greetings', c)
    print("_" * 70)

print()
print("_" * 70)
# WAP to print below pattern
"""
* 
* *
* * *
* * * *
* * * * *
"""
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    # print(j, end=" ") # with we can get clear picture how j is executing.
    print()

print("_" * 70)
# WAP to print below pattern
"""
* * * * *
* * * *
* * *
* *
* 
"""

for i in range(6, 1, -1):
    for j in range(0, i-1, 1):
        print("*", end=" ")
        #print(j, end=" ") # with we can get clear picture how j is executing.
    print()

