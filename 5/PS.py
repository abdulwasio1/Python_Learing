# fruits = ["Apple" , "Banana" , "Guava" , "Carot" , "Orange"]
# print(fruits[0])
# print(fruits[len(fruits) - 1])
# fruits.append("Grapes")
# fruits.append("Peach")
# print(len(fruits))
# vege = ("Potato" , "Cabbage" ,"Delicata")
# li = list[(vege)]
# fruits.append(li)
# print(fruits)



# name = input("Enter Name : ")
# age = input("Enter Age : ")
# Grade = input("Enter Grade : ")
# Subjects = []
# Subjects.append(input("Enter the Name of Subject 1 : "))
# s1 = input("Marks for Subject 1 : ")
# Subjects.append(input("Enter the Name of Subject 2 : "))
# s2 = input("Marks for Subject 2 : ")
# Subjects.append(input("Enter the Name of Subject 3 : "))
# s3 = input("Marks for Subject 3 : ")
# marks = {
#     Subjects[0]  : s1,
#     Subjects[1]  : s2,
#     Subjects[2]  : s3,
# }
# print("name" ," : " , name)
# print("Age" ," : " , age)
# print("Grade" ," : " , Grade)
# print("Subjects : " , marks)



# sentence = input("Enter the Sentence : ")
# print("Upper Case : " , sentence.upper())
# print("Lower Case : " , sentence.lower())
# print("Sentence length : " , len(sentence))
# print(sentence.replace(" " , "-"))
# print(sentence.startswith("The"))
# print(sentence.split("-"))



# print("1. Create Account \n 2. Login Account")
# code = input("Enter Choice : ")
# if code == '1' : 
#     rname = input("Enter Name : ")
#     rusername = input("Enter Username : ")
#     rCNIC  = input("Enter CNIC : ")
#     rgender = input("Enter Gender(M/F) : ")
#     rpassword = input("Enter Password : ")
# else : print("Enter Valid Number : ")

# enter = input("Press Enter to Login  ")
# username = input("Enter Username : ")
# password = input("Enter Password: ")
# if enter== chr(32) : 
#     if username== rusername and password== rpassword :
#         print("Login Successfully")
#     else : print("try again")



# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# operation = input("Enter operation (+, -, *, /): ")

# if operation == "+":
#     result = num1 + num2
# elif operation == "-":
#     result = num1 - num2
# elif operation == "*":
#     result = num1 * num2
# elif operation == "/":
#     if num2 != 0:
#         result = num1 / num2
#     else:
#         result = "Cannot divide by zero!"
# else:
#     result = "Invalid operation!"

# print("Result:" , result)
# print(f"Result: {result}") #f means f-string or formated string---> Python will exceute whatever in the bracket {} first, without f it will be treated as plain text




#STORE 9 and 9.0 as differnet elements in Set

#Solution 1 : Store as a Strings
number = {9 , "9.0"} #one value as a string
print(len(number))
print(number)

#Solution 2 : Store as Tuples with Type Info
number2 = {
    ("int" , 9), #In the form of tuples -> These Values are not key and value pair
    ("float" , 9.0)
}
print(number2)
print(len(number2))