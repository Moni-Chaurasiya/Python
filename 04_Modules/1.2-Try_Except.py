# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The else block lets you execute code when there is no error.

# The finally block lets you execute code, regardless of the result of the try- and except blocks.
x=10
try:
    f = open("virtualEnvironment.txt")
    try:
        try:
          print(x)
        except NameError:
          print("Variable x is not defined")
        else:
          print("Nothing went wrong")
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong")
    finally:
        f.close()
        print("finally will always execute")
except:
    print("Something went wrong when opening file")

# 10
# Nothing went wrong
# Something went wrong
# finally will always execute


# Perform Operations in F-Strings

price=49
txt=f"It is very {'Expensive' if price>20 else 'Cheap'}"
print(txt)

txt2="The price is {} dollor"
print(txt2.format(price))

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

#None is a special constant in Python that represents the absence of a value.
x = None
print(type(x))

print("Enter your name")
name= input()
print(f"hello {name}")

name = input("Enter your name:")
print(f"Hello {name}")

import cowsay # type: ignore
cowsay.cow("Good Mooooorning!")


