a=10
b= 200
if a<b:
    print("b is greater than a")  # indentation is must else you will gwt error

is_logged_in=True
if is_logged_in:
    print("Welcone back")
    
a=200
b=30
if b>a:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")
else:
    print("a is greater than b")
    
print("A") if a>b else print("B")

a=100
b=10

print("A") if a>b else print("=") if a==b else print("B")

c=150

if a>b and c>a:
    print("c is greater than a and b")

if a>b or a>c:
    print("a is greater than either b or c")

if not a>c:
    print("a is not greater than b")
    
score=80
attendance=90
submitted=True

if score >=60:
    if attendance >=90:
        if submitted:
            print("passed with good mark")
        else:
            print("passed")
            
    else:
        print("passed with good mark")
        
        
else:
    print("failed")
    if score>70:
        pass

# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

