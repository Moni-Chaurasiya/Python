# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
dict ={
    "name": "Moni",
    "age": 20,
    "roll": 8,
    "roll": 9  # duplicate will overwrite roll value
}
print(dict)
print(dict["roll"])

x=dict.get("age")
print(x)

y= dict.keys()
print(y)

dict["color"]="red"
print(dict)

z=dict.values()
print(z)

a= dict.items()

dict.update({"age":22})
print(dict)

for x in dict:
    print(x)  # all key 
    
for x in dict:
    print(dict[x])