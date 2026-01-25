# Encapsulation is about protecting data inside a class.

# It means keeping data (properties) and methods together in a class, while controlling how the data can be accessed from outside the class.

# This prevents accidental changes to your data and hides the internal details of how your class works.

# __age -->to crete variable private we use __ in python  

class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age # private 
        
    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        if age>0:
            self.__age=age
        else:
            print("Age must be positive")
            
            
p1 =Person("Moni",21)
print(p1.name)
# print(p1.__age) # it will give error

# Note: Private properties cannot be accessed directly from outside the class.
#  To modify a private property, you can create a setter method.


p1.set_age(22)
print(p1.get_age())

# Data Protection: Prevents accidental modification of data

# Validation: You can validate data before setting it

# Flexibility: Internal implementation can change without affecting external code



class Outer:
  def __init__(self):
    self.name = "Outer Class"

  class Inner:
    def __init__(self):
      self.name = "Inner Class"

    def display(self):
      print("This is the inner class")

outer = Outer()
print(outer.name)
inner = outer.Inner()
inner.display()


# An inner class is a class defined inside another class. The inner class can access the properties and methods of the outer class.

# Inner classes are useful for grouping classes that are only used in one place, making your code more organized.

