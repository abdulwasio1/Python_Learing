# with open("practice.txt" , 'w') as f:
#     f.write("Ho everyone \nwe are learning file I/O \nusing Java.\nI like Programming in Java" )


# Replace all occurances of Java with Python


# with open("practice.txt" , 'r') as f:
#     data = f.read()
# new_data= data.replace("Java" , "Python")
# print(new_data)
# with open("practice.txt" , 'w') as f:
#     f.write(new_data)


#Check "learning" exist in file or not

# def check(word):
#     with open("practice.txt" , 'r') as f:
#         data = f.read()
#     new_data = data.find(word)
#     if (new_data!= -1):
#         print("Eixsts")
#     else : print("Doesn't Exist")
# word = "learning"
# check(word)


#WAF to find in which line of file does the word "Python".
# lines = 1
# is_bool = False
# word = "Python"
# with open("practice.txt" , "r") as f:
#     for line in f:
#         if(word in line): # OR if(line.find(word) != -1)
#            print(word , "Word Found at" , lines) 
#            is_bool = True
#         #    break
#         lines = lines + 1
# if (is_bool== False): 
#     print("Does not Found returned -1")

# OR
'''
word = "Python"
line_no = 1
data = True --->when while loop become false data become false
with open("practice.txt" , "r") as f:
    while data:
        data = f.readline()
        if(word in data):
            print(line_no)
        line_no += 1    
'''

with open("numbers.txt" , 'r') as f:
    data = f.read()

#SCRATCH LOGIC
    
# num = ""
# for i in range(len(data)):
#     if (i==len(data) - 1):
#         num += data[len(data) -1]
#         print(num)
#     if(data[i]==","):
#         print(num)
#         num = ""
#     else:
#         num += data[i]

#SHORT METHOD ---> Spilt Method
# The split() method in Python is used to split a string into a list of substrings based on a specified separator like in this case comma is seperator
# SYNTAX --> string.split(separator, maxsplit)
# 1. separator (optional): The delimiter to split on. Default is whitespace.
# 2. maxsplit (optional): Maximum number of splits to perform. Default is -1 (all possible splits).

num = data.split(",")
# print(type(num)) It is a list
count = 0
#Now Convert each item of list into integer
for value in num:
    if(int(value) %2 == 0): #Typecasting
        count += 1
print(count)


   
    