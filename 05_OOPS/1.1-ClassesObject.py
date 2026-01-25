# OOP stands for Object-Oriented Programming.
# Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.

# Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.

x=1
class MyClass:
    x += 1

p1= MyClass()
print(p1.x)

p2= MyClass()
print(p2.x)

p3= MyClass()
print(p3.x)

# Each class is independent

class Person:
    pass
del p1  # to delete the object 


# All classes have a built-in method called __init__(), which is always executed when the class is being initiated.
# The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.
# The self parameter is a reference to the current instance of the class.
# It is used to access properties and methods that belong to the class.
# Without self, Python would not know which object's properties you want to access:

# instead of self we can give any name but it has to be first parameter of any method in the class


class Person:
    def __init__(self,name,age=18):
        self.name=name
        self.age=age


p=Person("Moni",20)
per=Person("Moni")
print(p.name)
print(p.age)

print(per.name)
print(per.age)


# Without the __init__() method, you would need to set properties manually for each object:
class Person:
    pass

p1=Person()
p1.name="Moni"
p1.age=25

print(p1.name)
# With __init__(), you can set initial values when creating the object:

class Person2:
    def __init__(myobj,name,age):
        myobj.name=name
        myobj.age=age
        
    def greet(abc):
        print("Hello my name is "+ abc.name)
    
    def display_info(self):
        print(f"{self.name}{self.age}")
        
p3= Person2("soni",20)
p3.greet()
p3.display_info()

# Methods are functions that belong to a class. They define the behavior of objects created from the class.

# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

class Student(Person2):
    # pass  # if we don't want to add any other properties or methods to the class
    def __init__(self,fname,lname,year):
        Person2.__init__(self,fname,lname)
        super().__init__(fname,lname)
        self.graduationyear=year

stu= Student("Monika", 20,2026)
print(stu.display_info())
print(stu.greet())
print(stu.graduationyear)


