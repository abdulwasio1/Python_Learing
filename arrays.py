import array

arr1 = [1,2,3,4,5]
print(type(arr1)) #Basically it is a list so HOW CAN WE ACTUALLY CREATE AN ARRAY

'''
import array -- importing module

arr = array.array(typecode, [values])
Two things required:

typecode — what type of data - it is basically unicode letter for defining type of data 
values — initial values

'b' signed integer    1 byte
'B' unsigned integer  1 byte
'i' signed integer    2 bytes
'I' unsigned integer  2 bytes
'l' signed integer    4 bytes
'f' float             4 bytes
'd' double/float      8 bytes
'u' unicode char      2 bytes
'''

# print(arr1[0] + arr1[3])

arr2 = array.array('i' , [1,2,3,4,5])
# print(arr2)

# for i in arr2:
#     print(i)

# print(type(arr2))

arr3 = arr1 # not copying the value but it copying the reference - means it is pass by reference changing one will change other
# print(arr1)
# print(arr3)
# arr3[2] = 45
# print(arr1)
# print(arr3)

# WE CAN AVOID THAT ABOVE PROBLEM like sometimes we don't want to change both so we can fetch list values from one array and store it into 2nd array

arr4 = array.array('i', arr2.tolist())
# tolist() creates a brand new list → then a brand new array is made from it.
# So arr2 and arr4 are completely separate in memory , Changing arr2 does NOT affect arr4 at all!
print(arr2)
print(arr4)
arr2[2] = 45
print(arr2)
print(arr4) #bcz it creates seperate independent memory

# GENERATOR EXPERSION
arr5 = array.array('i' , (n for n in arr2))
# It means:
# "Give me each n, for every n in arr1"
'''
first  → 33
second → 4
third  → 55
fourth → 5
fifth  → 66
Why () and not []?
[n for n in arr1]   # List Comprehension  → creates full list in memory
(n for n in arr1)   # Generator Expression → gives items ONE BY ONE
'''

# This is just another way to copy arr1 into arr2 — same as tolist() but using a generator. It is memory efficent
# arr1 = array('i', range(10_000_000))  # 10 million items!
# tolist() → creates 10 million item list in RAM first 😬
# Generator → passes items one by one, no extra RAM needed. It does not store values it just remember which one references to which one so it just call 