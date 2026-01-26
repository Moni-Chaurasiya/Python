# The Python enumerate() function is a built-in utility that adds a counter to any iterable object (like a list, tuple, or string) and returns it as an enumerate object. 
# This makes it a Pythonic and efficient way to access both the index and the value of each item simultaneously during iteration, typically within a for loop. 

x=("masala","lemon","ginger")
y= enumerate(x)
print(y)
print(list(y))  # [(0, 'masala'), (1, 'lemon'), (2, 'ginger')]

file= open('test.py',"w")  # if file is not there then it will create it

try:
    file.write('chai aur code')
finally:
    file.close()
    #  OR
with open('test.py','w') as file:
    file.write("Moni Chaurasiya") 