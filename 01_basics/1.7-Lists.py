# List is a collection which is ordered and changeable. Allows duplicate members. Can contain different Data Types
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members. Can contain different Data Types
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
# array have same methods and properties as List. Array can store same dataType. List can be used instead of array
# to work with arrays in Python you will have to import a library, like the NumPy library.

List=["apple","banana", "cherry","apple"]
print(List[1]) # print second item
print(List[-1]) # print last item
print(List[:])  # all value 
print(List[1:])  # index 1 to last
print(List[:3])  # beginning to 2nd index -> exclude 3
print(List[-3:-1]) # banana to cherry not include last -1 index


if "apple" in List:
    print("apple is present")


List[1]="grapes"

List.insert(4,"watermelon") # insert at 4th index
print(List)

List.append("orange") # add at last

SecondList=["river","mountain"]

List.extend(SecondList) 
# we can append any iterable object tuple, sets, dictionaries

print(List)

List.append("banana")
List.remove("banana") # remove specified item
print(List)
List.pop(1) # remove specified indexed value

for i in range(len(List)):
    print(List[i])
   

# del List[0]
print(List)
# List.clear() # remove all content

fruits=[]
for x in List:
    if "a" in x:
        fruits.append(x)
        
print(fruits)        
# we can use List Comprehension for above code
newList=[x for x in fruits if "e" in x]
print(newList)

anotherList=[x for x in newList if x != "apple"]
print(anotherList)

Lists=[x for x in range(10) if x!=0]
print(Lists)
List.append("banana")
fruit=[x if x!= "banana" else "orange" for x in List]
print(fruit)

fruit.sort()
print(fruit)

fruit.sort(reverse= True)
print(fruit)

def fun(n):
    return abs(n-5)

Lists.sort(key=fun) # sort the list on how close the number is to 50
print(Lists)  

thisList= List.copy()
print(thisList)

thisLists=list(List)

