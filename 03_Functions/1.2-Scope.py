# A variable is only available from inside the region it is created. This is called scope.
# If you use the global keyword, the variable belongs to the global scope:

z=100  # global scope
def myfunc():
    
    x=300  # local scope
    y=200
    global a
    a=150
    def myinnerfunc():
       nonlocal x
       x="hello"
       print(x)
    myinnerfunc()
    print(y)
    print(z)
    print(x)
    
myfunc()

print(a)