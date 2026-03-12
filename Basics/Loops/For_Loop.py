# Vd 15 : Python for loop, Session 1, Revision on 12/03/2026

# For loop: When we want to repeat instant for number of time.
"""
for cond:
    code

"""
# when dealing with number we use range function.
# range (start, stop, difference)
# when we run loop with range, than it included the start value and exclude stop value.

for i in range(1, 10, 1):
    print(i)

# range with 2 parameter (start, stop), default difference will be 1.
for j in range(11, 19):
    print(j)

# print negative values in reverse order.
for k in range(-11, 0, 1):
    print(k, end="")

print("_" * 70)
# range with one parameter, range (stop_value), default initial value will be 0 and difference value will be 1.
for q in range(15):
    print(q, end="")

# for q in range(0.5, 9.9, 1):
#     print(q, end="") # TypeError: 'float' object cannot be interpreted as an integer

"""
# range class rule
1. range accepts three parameters start, stop, and difference. range(start,stop,step)
2. range output include start value and exclude stop value
3. if we don't define initial value then default initial value will be zero. range(5)
4. range parameter only accepts integer value, float value is not allowed.
5. if we define 2 parameter in range, then it will consider initial value start value, stop value.
   -> difference value will be 1.
   range(2, 10) -> start=2, stop=10, step=1
"""

print("_" * 70)
# apply if condition in the loop
# WAP to get all the number which are divisible by 7 between 1 and 50
for i in range(1, 50, 1):
    if i % 7 == 0:
        print(i, end=" ")


print()
print("_" * 70)
# WAP to print table of any given number.

num = 8
for i in range(1, 11):
    print(i, "*", num, "=", i * num)
"""
1 * 8 = 8
2 * 8 = 16
3 * 8 = 24
4 * 8 = 32
5 * 8 = 40
6 * 8 = 48
7 * 8 = 56
8 * 8 = 64
9 * 8 = 72
10 * 8 = 80
"""

# apply loop in list
list1 = [2, 4, 6, 7, 8, 10, 13, 99]
for val in list1:
    print(val, "Square value : ", val ** 2)