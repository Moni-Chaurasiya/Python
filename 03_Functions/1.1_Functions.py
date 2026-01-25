# A function is a block of code which only runs when it is called.

# A function can return data as a result.

# A function helps avoiding code repetition.

def myFun():
    print("this is function")

myFun()

# A function name must start with a letter or underscore
# A function name can only contain letters, numbers, and underscores
# Function names are case-sensitive (myFunction and myfunction are different)

def fahrenheit_to_celcius(n):
    return (n-32)*5/9

x=fahrenheit_to_celcius(100)
y=fahrenheit_to_celcius(50)

print(x)
print(y)

def fullName(first,last):
    print(first+ " "+ last)

fullName("Moni","Chaurasiya")

def fullName(*,first="a",last="b"):  # default value if argument is not passed at the time of call
    print(first+ " "+ last)

fullName()

# When you call a function with arguments without using keywords, they are called positional arguments.


fullName(first="Moni")
# fullName("Moni","Chaurasiya")  # Error because fullName function is key-only argument as * is added before parameter

def person(person,/):   # here / means positional argument and if you try to use keyword argument then it will give error
    print("Name:",person["name"])

personName={"name":"Moni","age":25}

person(personName)

def function():
    return (2,10)

(x,y)=function()

print("x:",x)
print("y:",y)

# *args and **kwargs
# By default, a function must be called with the correct number of arguments.

# However, sometimes you may not know how many arguments that will be passed into your function.

# *args and **kwargs allow functions to accept a unknown number of arguments.

def my_func(*Kids):
    print(type(Kids))  # tuple
    print("The youngest child is "+ Kids[2])

my_func("Moni","Soni","Avanish")

# The *args parameter allows a function to accept any number of positional arguments.


def functions(greeting, *names):
    for name in names:
        print(greeting,name)


functions("Hello","Moni","Soni","Avanish")

# If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.

def person_Name(**Kids):
    print("Name of person is " +Kids["fname"])
    
person_Name(fname="Moni", lname="Chaurasiya")


def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")

def sum(a,b,c):
    return a+b+c
num=[1,2,3]
result=sum(*num)
print(result)


def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person)