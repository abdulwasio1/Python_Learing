#Set is Collection of the Unordered items, where each element in the set must be unique and immutable
#Elements in the set must be immutable (int , float , boolean , string , tuple) 
#but set never contain lists and dictionaries because they both are mutable

set_of_numbers = {1,2,3, "Hello" , 2 ,"Wasio"}

#NOTE : SET unordered ha means zaroori nhi jo chz ham na phle likhe ha set ma wo phle aye gi

#Duplicates values are ignored (Last Values) by Python. Doesn't put an error
#Dictionaries contain key value pair but set contain only values

print(set_of_numbers)
print(type(set_of_numbers))
print(len(set_of_numbers)) #Length method also ignore duplicate values


#HOW TO CREATE EMPTY SET?
collection = {}
print(type(collection)) #But it is a dictionary so we can create empty set using "set" keyword
collection1 = set() #This is now empty set
print(type(collection1))

#SET METHODS
set_of_numbers.add("Added_Value") #Add the provided value
# set_of_numbers.add([5,4,6]) #We are trying to add list inside the set which will put an error of "unhashable type" bcz lists are mutable
set_of_numbers.add((7,3,8)) #We are trying to add tuple inside Set which is acceptale bcz tuples are immutable and can be changed
set_of_numbers.remove("Wasio") #removes specific element
set_of_numbers.pop() #removes a random value
print(set_of_numbers)
set_of_numbers.clear() #empty the entire set
print(set_of_numbers)

#UNION AND INTERSECTION
set1 = {1,2,3,4,5}
set2 = {4,3,6,7,2}
print("Union of Both Set is : ",set1.union(set2)) #combines both values and return new Set
print("Intersection of Both Set is : ", set1.intersection(set2)) #combines Comman values and return new Set
print(set1) #DOES NOT AFFECT ORIGINAL SET
print(set2) #DOES NOT AFFECT ORIGINAL SET

#NOTE : Python sets itself are "MUTABLE" (bcz we can add and remove elements ) — but their elements must be "IMMUTABLE".

'''
HASHABLE AND UNHASHABLE VALUES

1. HASHABLE VALUES
A value is hashable if:
It has a hash value (__hash__() exists)
That hash value never changes during its lifetime
It can be compared for equality (__eq__()
--> A hash is just a fixed integer generated from an object.

2. UNHASHABLE VALUES
A value is unhashable if:
It can change (mutable)
Python cannot guarantee a stable hash

Common hashable vs unhashable types
✅ Hashable -> Constant
int
float
bool
str
tuple (only if all elements are hashable)
frozenset
None

❌Unhashable -> Variable or Changeable
list
dict
set
bytearray


✔️ Critical rule (interview gold)
1️⃣ All dictionary keys must be hashable.
2️⃣ All set elements must be hashable.
'''