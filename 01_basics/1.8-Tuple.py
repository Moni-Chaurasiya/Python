# Tuple Items
# Tuple items are ordered, unchangeable, and allow duplicate values.

# Ordered
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# Allow Duplicates
# Since tuples are indexed, they can have items with the same value:

tuple1 = ("abc", 34, True, 40, "male") # can contain different data Types
print(type(tuple1))

# Unpacking tuple

fruits= ("apple", "banana", "grapes")
(a,b,g)=fruits
print(a,b,g)

# Using Asterisk*
# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

fruit = ("apple", "banana", "cherry", "strawberry", "raspberry")
(a,b,*c) = fruit
print(a,b,c)  # here c is a list 

myTuple=fruits*2 # it will add item twice 
print(myTuple)



