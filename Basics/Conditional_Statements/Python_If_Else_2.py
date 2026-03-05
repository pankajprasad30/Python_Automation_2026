# Vd 13 : Python if-else basics, Session 2, Revision on 05/03/2026
"""
# Logical operators :-
>  : Greater than
<  : Less than
>= : Greater than equal to
<= : Less than equal to
!= : Not equal to
== : Equal to operator
in : in operator
is : is operator
is not : is not operator

And Logic :
True and False : False
False and True : False
False and False : False
True and True : True

Or Logic :
True and False : True
False and True : True
False and False : False
True and True : True


"""

"""
if cond1 :
   code
elif cond2:
   code
elif cond3:
   code
else:
    code
"""

# WAP to check greater number among three
a = 100
b = 100
c = 20

if a > b and a > c:
    print ("A has greater value: ", a)
elif b > a and b > c:
    print("B has greater value: ", b)
elif c > a and c > b :
    print("C has greater value : ", c)
elif a == b == c:
    print("A, B, C has equal value ")
elif a == b != c:
    print("A, B has equal value")
else:
    print("No one has greater value")

print("_" * 70)
# WAP to provide grade to the student as per marks obtained.
marks = 95

if marks > 35 and marks <= 50:
    print("Pass with c grade")
elif marks > 50 and marks <= 70:
    print("Pass with b grade")
elif marks > 70 and marks <= 90:
    print("Pass with a grade")
elif marks > 90 and marks <= 100:
    print("Pass with excellent grade A++")
elif marks > 100:
    print("Invalid marks")
elif marks < 0:
    print("Invalid marks")
else:
    print("Better luck next time")

print("_" * 70)
# WAP to check the given number is divisible by 3 or 7
A = 50
if A % 3 == 0 or A % 7 == 0:
    print("A is divisible by 3 or 7 ")
else:
    print("A is not divisible by 3 or 7")

# Vd 14 : Python if-else basics, Session 2, Revision on 05/03/2026