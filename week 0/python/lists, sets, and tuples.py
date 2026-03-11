List = []
Set = {}
Tuple = ()

fruits = ["apple", "banana", "cherry"]
#print(dir(fruits)) #list of all func
#help(fruits) # every func
# "apple" in fruits # true/false
fruits.append("apple2")
fruits.remove("banana")
fruits.sort()
fruits.insert(1,"orange")
fruits.reverse()
fruits.clear() #del all elements
fruits.count("orange")

fruits = {"apple", "banana", "cherry"}
#print(dir(fruits))
#help(fruits)
fruits.add("apple2")
fruits.remove("banana")
fruits.clear()

fruits = ("apple", "banana", "cherry")
print(dir(fruits))
help(fruits)
fruits.index("apple")
fruits.count("apple")
len(fruits)
# "apple" in fruits #true/false
