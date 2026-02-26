# Vd 10 : Python Data Type Session 3, Revision on 26/02/2026

print("_" * 70)
##################### Set data type ######################
set1 = {55, 22, 3, 5.5, 6, 7, 3, 3, 2}
print(set1, type(set1)) # {2, 3, 5.5, 6, 7} <class 'set'>
# Set will Automatically remove duplicate data

"""
# Properties of set data type:
1. Set is a mutable data type, we can modify any point of time.
2. Set only store unique values, Duplicate data is not allowed.
3. Set store data in random order and print values in random order.
4. Set only contains immutable data type as set member.
  -> int, float, string, tuple, boolean
5. Set doest not follow any indexing or key value pair format.
"""

set2 = {44, 72, 'hello', (2, 3, 4), True, True, 44}
print(set2)

tup1 = (4, 6, 6, 6, 9)
print(tup1) # it stores duplicate

# Add values to the set.
set2.add(30)
print(set2)
set2.add(30) # it won't give error if we try to add same value again.
print(set2)

print("_" * 70)
print(dir(set))
"""
'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 
'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 
'union', 'update']

"""

# set3 = {3, 4, 6, 7, [2, 6, 9, 10]} #
# print(set3) #TypeError: unhashable type: 'list'
# Can not add list/dict/set as member of set
# list/dict/set is mutable data type which is not allowed in the set.


print("_" * 70)
##################### Boolean data type ######################
# Boolean sata type only cotains two values which is True and False.

var1 = True
print(var1, type(var1))

var2 = False
print(var2, type(var2))

print(dir(bool))
#as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag',
# 'is_integer', 'numerator', 'real', 'to_bytes'

print(var1.to_bytes())