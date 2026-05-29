def good(value):
    value = value ** 2 #--->  "**" means a ^ b
    return value

result = good(3)
print(result)



def hello(to="world"):
    print("hello,", to)
# to="world" is a default parameter — if no argument is passed, to automatically becomes "world"
# to="world" in a function definition is NOT a regular assignment
# Context                            Meaning
# to = "world" (outside function)    Regular variable assignment
# def hello(to="world"):             Default parameter value

hello()
name = input("What's your name? ")
hello(name)



# for i in range(5):
#     print(good(i))

# def wish(name):
#     gr = ("Happy Birthday" , name)
# a  = wish("Wasio")
# print(a)   #It will print None bcz function return nothing and nithing is stored in a variable

# def wish(name):
#     gr = ("Happy Birthday" , name)
#     return gr
# a  = wish("Wasio")
# print(a)

# def cal(list2):
#     for i in range(len(list2)):
#         for j in range(i+1, len(list2)):
#             if(list2[i]<list2[j]):
#                 list2[i] , list2[j] = list2[j] , list2[i]
#     print(list2)
# list2 = [2,4,7,3,7,2]
# cal(list2)

'''

            SWAPING METHOD IN PYHTON
1.
                temp = list2[i]
                list2[i] = list2[j]
                list2[j] = temp
2.
                list2[i] = list2[i] ^ list2[j]
                list2[j] = list2[j] ^ list2[i]
                list2[i] = list2[i] ^ list2[j]
3. 
                list2[i] , list2[j] = list2[j] , list2[i] (Doesn't work in C++/Java)

4.
                a = (a+b) - (b = a) --> But it doesn't work in Python (for C++/Java)

'''


#RESCRUSION

# def fac(num):
#     if(num==1 or num==0):
#         return 1
#     return ( num * fac(num-1))
# a = fac(6)
# print(a)

# def sum(nums):
#     if (nums==1 or  nums==0):
#         return 1
#     return (nums + sum(nums-1))
# value = 50
# sums =  sum(value)
# print(sums)

# def pattern(n):
#     multi = 1
#     if(multi<=n):
#         print("*" * multi)
#     else : return " "  
    
#     multi += 1
#     pattern(n+1)
# pattern(5)

# def triangle_increasing(n, current =1 ):
#     if current > n:
#         return
#     print('*' * current)
#     triangle_increasing(n, current + 1)
# triangle_increasing(5)    


# def remove(names , str):
#     item = []
#     for i in names:
#         if not(str==i):
#             item.append(i.strip(str)) #strip doesn't work on lists
#     return item

# names = ["wasio" , "hellio" , "pollio" ,"io"]
# str = "io"
# print(remove(names , str))

# name = "Wasio"
# print(name.strip("Was"))

