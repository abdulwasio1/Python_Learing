#in Pyhton Array are known as Lists but there are several differences from other languages
'''
What a Python list actually is

A Python list is NOT an array of values.
It is an array of references (pointers).

Example
lst = [10, "hello", 3.5]


Internally:

[list]
  ├── pointer → 10 (int object)
  ├── pointer → "hello" (str object)
  └── pointer → 3.5 (float object)

Key properties
Property ->	Python List
Size  ->	Dynamic
Data type  ->	Mixed allowed
Memory  ->	Array of references
Speed  ->	Slower than real arrays
Flexibility  ->	Very high

Why Python list is slower

Extra indirection (pointer → object)
Every element is a full object
Type checking at runtime
'''
list = [1,4.45,"Hello" , 'S' , True]
# print(list)
# print(list[0])
# print(list[4])
# print(list[2] , "-> Old Value")
# list[2] = "Wasio" #We can change values in List at any index but we can't do in Strings because Strings are Immutable
# #but Lists are mutable
# print(list[2], "-> Updated Value")

# #SLICING OF LISTS IS EXCATLY SAME AS STRINGS
# print(list[1:4])
# print(list[-3:])
# print(list[:-1])

#METHODS IN LISTS(Modify Lists, doesn't create new List ) 

list.append("Shaikh")
print(list)
list2 = [7,2,0,-3,5,1,4,14]
list2.sort() #Only for Numbers(Low to High) - > Acesnding Order
list2.sort(reverse=True) # High to Low -> Descending Order
print(list2)
list.reverse() 
list2.reverse()
print(list)
print(list2)
list2.insert(2,20002)
print(list2)
list2.pop() #remove from last index and return that removed value
print(list2.pop(2)) #print that remoevd value
print(list2)
list2.pop(3) #reomve value at index 3
print(list2)
list2.remove(1);
print(list2)
# list2.clear()
list2.append(2)
print(list2)
print(3 in list2) #fALSE bcz 3 is not this list
print(2 in list2) #fALSE bcz 3 is not this list
print(type(list2)) #Class Type LIST
print("The Frequency of 2 in this list is : ", list2.count(2)) #count the frequency of Given number in list
list3 = [1,2,3]
print(list3 * 3)
print(list3 + [3,4,5])


fruits = ["apple", "banana", "mango"]

print(fruits[0])    # apple   (first)
print(fruits[-1])   # mango   (last)
print(fruits[1:3])  # ['banana', 'mango']  (slicing)
