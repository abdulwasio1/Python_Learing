'''
Decorator is a function that takes a function as input, 
adds extra behavior to it, and returns a new modified function 
without changing the original function's code!

Decorator = Extra kaam + Tumhara function — bina original code chhede!

Technical Definition:
A decorator is a Higher Order Function that:

1. TAKES  → a function as argument
2. ADDS   → extra behavior around it
3. RETURNS → a new wrapped function

WHY RETURNS WRAPPED
bcz @decorator always expect a function in return - Higher order function 
        |
        v
        say_hello = decorator(say_hello) ---> with return
        say_hello = None ---> Without return
say_hello will become whatever decorator returns!

Question : if without return it gets 'None' then whats the error it just print none simple?
Answer : 
say_hello = None   # decorator returned nothing
say_hello() # you are doing None()  ← THIS is the problem!

You are trying to call None like a function!
None is not a function — it cannot be called!
'''
# def access(func):
#     def message():
#         print("Access Granted")
#         func()
#     return message

# @access #----> welcome = access(welcome)
# def welcome():
#     print("Welcome to Dashboard")

# welcome()


# def run(func):
#     def print_message():
#         for i in range(3):
#             func()
#     return print_message

# @run
# def say_hello():
#     print("hello")

# say_hello()


# def uppercase_decorator(func):
#     def wrapper():
#         # Just call the function and capture return value
#         result = func()
#         print(result.upper())
#     return wrapper

# @uppercase_decorator
# def say_hello():
#     return "hello my name is ali"  # use return instead of print!

# say_hello()

# Output:
# HELLO MY NAME IS ALI
        
count = 0
def count_decorator(func):
    def wrapper():
       func()
       global count 
       count += 1
    return wrapper

@count_decorator
def message():
    print("Hello")

message()
print(count)