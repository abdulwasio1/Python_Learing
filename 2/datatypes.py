a = 10 #comlier automatic understand it is integer during runtime
print(type(a)) #type() function is used to find the datatype of variable
b = "Wasio"
print(type(b))
c = 21.4
print(type(c))

#TYPECASTING

e = 23.45 #it is float bydefault in PY
print(int(e)) #Float to int
f ="12"
print(int(f)) #String to Int


#Input in PY using "input" keyword
x = input("Enter Num 1 : ")
y = input("Enter Num 2 : ")
print("First Number is : ", x) 
print("Second Number is : ", y)
print("The Sum of Num1 and Num2 is : ", x + y) #integer addition will not perform there, here every output is a string so "+" sign concatenate 
print("The Sum of Num1 and Num2 is : " , int(x+y)) # this will again same but here first string concatenate then typecast
#DO IT LIKE
j = int(input("Enter Num 1 : "))
k = int(input("Enter Num 2 : "))
print("The Sum of both numbers are : " , j + k)

