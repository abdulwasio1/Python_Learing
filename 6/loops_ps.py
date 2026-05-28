# import math
# n = int(input("Enter the Value of n : "))
#SUM OF FIRST N
# sum = 0;
# while n>0 :
#     sum += n
#     n-=1
# print(sum)  


#FACTORIAL
# product = 1
# for i in range(n):  #-----> for i in range(1, n+1) is also correct
#     product *= n
#     n-=1
# print(product)


# Count Even Numbers
# count = 0
# for i in range(1, 51) :
#     if(i%2==0) :
#         count += 1
# print(count)


# Fibonacci Sequence
# n = int(input("Enter Number : "))
# a = 0
# b = 1
# i = 0 
# while i < (n-1) :
#     c = a+b
#     a = b
#     b = c
#     i = i +1
# print(c)

#PRIME CHECKER
# n = int(input("Enter Number : "))
# i = 2
# if n==0 or n==1 : print("Neither Prime nor Composite")
# exit()
# while i < math.sqrt(n):
#     if(n%i==0) :
#         print("It is composite on " , i)
#         break
#     i = i +1
# else : print("It is Prime")    


#Pattern
# for i in range(5):
#     for j in range(i+1):
#         print("*" , end=" ")
#     print()   

# List Operations
# numbers = [12, 75, 150, 180, 145, 525, 50]
# for i in numbers :
#     if(i%5==0 and i<=150) : print(i)

# Number of Digits
n = 3435567
temp = n
count = 0
while n > 0 : 
    n = n//10
    count +=1
print("The Number of digits in " , temp , " is " ,count)
