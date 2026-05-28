set1 = set("abc")
set2 = {'e' , 'b', 'c' , 'b'}
# print(set[0]) # Error bcz Sets are UNORDERED & UNINDEXED Subscriptable means "can be accessed by index []"
# Sets are NOT subscriptable — they have no index!

# print('a' in (set1 and set2))
print(set1)
print(set2)

# SETS CAN BE CONVERTED INTO LISTS
listA = list(set1)
listB = list(set2)
print(listA[1])
print(listB[1])
print(set1- set2) #Works same as difference in Math sets
print(set1 | set2) #UNION
print(set1 & set2) #INTERSECTION
print(set1 ^ set2) #Symetric difference - removes comman and print remaining