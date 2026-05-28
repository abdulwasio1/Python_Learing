# a = 0;
# while a<5 :
#     print("Hello")
#     a = a + 1 
    
#     print("Loop End")


#INDENTATION IN LOOPS
'''
Upper Loop will print Hello + Loop End Every time
But Lower Loop will prine Hello Every time and in last Loop End just bcz of indentation (leading Space )
Indended Code(with spaces) -> runs inside the loop
No Indentation -> runs after the loop ends

'''

# a = 0;
# while a<5 :
#     print("Hello")
#     a = a + 1 

# print("Loop End")
    

#FOR LOOP SYNTAX


#for variable_name in list/tuple/string name : 
#    print(variable_name)    
    
# str = "Abdul Wasio"  
# numbers = [1,3,6,36,53]
target = 3
# tup = ("Hell0" , "Kya Hal ha" , "12" , 34.64 , 124 , True)
tup2 = (2,4,6,5,7,4,57,3,2)
for num in tup2 : 
    if(num==target) :
        print("Found") 
        break
else : print("Not Found")

#NOTE : Here else condition loop ki ha na ki if(num==target) ki, Proof : Agar loop ki hoti to else wala bar bar print hota lkn agr loop ki hoti to jab loop end hojta tab sirf ak bar chalte 


#RANGE OBJECTS

for x in range(5) :  #range start from 0 
    print(x)
print("\n")
for y in range(2,8) :
    print(y)    
print("\n")    
for z in range(1,10,2): #(Start , end , gap) 1 3 5 7 9 ---> end is necesaary if we write only one it must be "end"
    print(z)
print("\n")
for a in range(5 , 0 , -1) :  # 5 4 3 2 1 
    print(a)


#IN DICTIONARIES
collection = {
    "name" : "Abdul Wasio",
    "Class" : "BSCS",
    "Age" : 19,
    "Grade" : 'A'
}

#For Keys of Dictioaries   
for keys_ in collection : #BY DEFAUT IT WILL PRINT KEYS
    print(keys_)
print("\n")  

#For Values of Dictioaries  
for values_ in collection.values(): #.values sets loop to print values of collection dictionary
    print(values_)   
print("\n") 

#for key value pairs
for keys,values in collection.items() : 
    print(f"{keys} : {values}") # We can also write print(keys," : " ,  values)


#IN SETS
print("\n")  
set_collection = {1,2,3,4,5}
for value in set_collection :
    print(value)

#PASS STATMENT : Pass is Null Operation or no Operation statement in PY. It does nothing when executed
#USAGE : 
# Place Holder for future code (Most Common)
#2. Can aslo used instead of comments
# --> Leaving a Block empty is not allowed in Python bcz -----
                                                        #    |
                                                        #    v
#Basically Python uses indentation to define code blocks, not braces {}
#like in C++/Java Empty block is allowed but in PY it's not so we use pass statement
for i in range(5):
    pass
print("Above Loop is passed ")