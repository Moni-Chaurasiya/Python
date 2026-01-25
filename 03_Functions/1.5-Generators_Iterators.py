# Generators are functions that can pause and resume their execution.
# When a generator function is called, it returns a generator object, which is an iterator.
# The code inside the function is not executed yet, it is only compiled. The function only executes when you iterate over the generator.

from ast import Import


def my_generator():
    yield 1
    yield 2
    yield 3

for values in my_generator():
    print(values)
    
# Generators allow you to iterate over data without storing the entire dataset in memory.
# Instead of using return, generators use the yield keyword.
# The yield keyword is what makes a function a generator.

def count_up_to(n):
    count=1
    while count<=n:
        yield count
        count +=1
        
for num in count_up_to(5):
    print(num)


# Generators are memory-efficient because they generate values on-the-fly instead of storing everything in memory.

# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

# All these objects have a iter() method which is used to get an iterator:

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
 
print(next(myit))
print(next(myit))
print(next(myit))

# an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

person1={
    "name": "moni",
    "age": 21,
    "country": "India"

}

