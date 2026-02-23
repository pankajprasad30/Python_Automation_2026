# Vd 6 : Python Variable Session1, Revision on 23/02/2026
a = 10
# a : Variable
# = : Is called assignment operator
# 10 : Value assign to the variable
# Python is dynamic programmable language that's why we are not declaring any data types.

print(a) # 10
# id will give you the location where my value is getting stored.
print(id(a)) # 140721308959944

b = 20
print(id(b)) # 140721406936584
# Every different variable having different value will have different address.

# now lets check if two variable with have same value #
# If two variable have same value, then their address will be same.
x = 40
y = 40
print(id(x)) # 140721245718664
print(id(y)) # 140721245718664

print("X :", x, "Address: ", id(x)) # X : 40 Address:  140721308960904
print("Y :", y, "Address: ", id(y)) # Y : 40 Address:  140721308960904

########### Assign multiple value to multiple variable at a time #############
p, q, r = 10, 20, 30
print("Value of p :", p)
print("Value of q :", q)
print("Value of r :", r)
print("Value of p, q ,r : ", p, q, r)