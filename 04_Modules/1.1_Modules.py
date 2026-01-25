import platform

x=platform.system() 
print(x)
y=dir(platform) # List all the defined names belonging to the platform module:
print(y)

import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A")) 
# %A means Weekday, full version -> Monday
# %a means Weekday, short version -> Mon
# %d means Day of month 01-31 -> 31
# %B means Month name, full version -> December
# etc refer documention




time = datetime.datetime(2026,1,25)
print(time)

print(min(5,20,45))
print(max(6,3,2))

print(abs(-7.25))

print(pow(4,3))

import math
s=math.sqrt(64)
print(s)
lower=math.floor(1.4) #1
upper=math.ceil(1.4) #2
print(lower)
print(upper)

pi= math.pi
print(pi)


# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.
import json

x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y= json.loads(x)

print(y["age"])


z = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
a = json.dumps(z)

# the result is a JSON string:
print(a)

# Convert Python objects into JSON strings, and print the values:
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


# RegEx
import re

txt="Moni Chaurasiya"
name= re.search("^Moni.*Chaurasiya$",txt)
if name:
    print("Yes Matched")
else:
    print("No Match")



import camelcase

c=camelcase.CamelCase()
txt="hello Moni"

print(c.hump(txt))

