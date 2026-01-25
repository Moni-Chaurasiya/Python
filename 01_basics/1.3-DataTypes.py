# Mutable Data types -->> List, Set, Dictionary, Bytearray, Array
# Immutable Data types -->> Integers, Floating-point numbers, Boolean, Strings, Tuples, Frozen set, Bytes

# Mutable means value can be change inside memory
# Immutable means value cannot change -> only reference will change -> that is variable point to other value, if we assign any other value to that variable.
# In python data type is given only to the value not to the variables
# In python variable don't have any dataTypes, variable is used only for reference the value
a=10   # a point to 10 
a=20   # a point to 20 and it will not replace 10 instead new memory will assign for 20 and a reference to 20

# In Python everything is Object
import math
import random

print(12+12)
print(12+12.5)
print(2**100)

print(math.pi)
print(random.random())
print(random.choice([1,2,3,4,5]))

username="MoniChaurasiya"
print(len(username))

print(username[0])

# username[0]='a'  --->> Error as string is immutable

print(username[-1]) # Last Value will print
print(username[-2]) # Second Last
print(username[1:3]) # 3 is not included

# print(dir(username))


myList=[123,"moni",3.14]
print(myList)
print(len(myList))
# print(myList[-4])   error -> list index outof range

dictionary={1:'one', 2:'two', 3:'three'}

print(dictionary[1])  #  Access by key

myTuple=(1,2,3)
print(myTuple[0])

import sys

# In python there is no any way to get reference or reach close to memory therefore we get same value every time
refCount=sys.getrefcount(243)
print('reference count for 243',refCount) # 4294967295

refCountString=sys.getrefcount('moni')
print('reference count for moni',refCountString) # 5


refCounts=sys.getrefcount(24344)
print('reference count for 24344',refCounts) # 3

refCountStrings=sys.getrefcount("monii")
print('reference count for monii',refCountStrings) # 3

refCountss=sys.getrefcount(243)
print('reference count for 243',refCountss) # 4294967295

a=10
a='moni'
print(a)

a1=[1,2,3]
a2=a1

a1[0]=20   # a2 will also change because a2 have assigned the reference of a1
print(a2)   

m1=[1,2,3]
m2=m1[:]
print(m1==m2) # True  -> because value is same 
print(m1 is m2)  # false -> because reference is not same 
m1[0]=30  # m2 will not modified because it is given copy of m1
print(m1)
print(m2)

import copy
m2=copy.copy(m1)
print(m1==m2)
m2=copy.deepcopy(m1)




