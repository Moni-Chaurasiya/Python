# Decorators let you add extra behavior to a function, without changing the function's code.
# A decorator is a function that takes another function as input and returns a new function.

def changeCase(func):
    def innerFunc():
        return func().upper()
    return innerFunc

@changeCase
def greeting():
    return "Hello Moni"  

print(greeting())  # HELLO MONI

import functools
#Import functools.wraps to preserve the original function name and docstring.

def changecase(n):
    
  def changecase(func):
    @functools.wraps(func)
    def myinner(*args,**kwargs):
        if n==1:
          return func(*args,**kwargs).lower()
        else:
          return func(*args,**kwargs).upper()
      
    return myinner
  return changecase

#@changeCase # we can add multiple decorator
@changecase(0)
def greet(nam):
    return "Hello" + nam

print(greet("Moni"))


print(greeting.__name__)  # function have metadata

