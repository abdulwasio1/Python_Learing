# Python has function order issue like a function must exists before calling not like java

# hello()
# def hello():

# ABOVE WE GOT ERROR THAT HELLO NAME DOES NOT EXITS
# so we can solve through :  Functions Calling Each Other Technique

def a():
    print("I'm a!")
    b()  # b() not defined yet... but it's okay!

def b():
    print("I'm b!")

a()  # ✅ Works fine  

# How this works --> When Python hits def a(): it just goes: 
# "Okay, a is a function, I'll save it — moving on" 🏃
# It skips the body completely and goes to the next line
# So def just registers the function in memory. 
# Python only reads the body when you actually call it with ().


def main():
    name = input("Enter Your Name : ")
    hello(name)

def hello(name = "Tommy"):
    print("Hello , " + name )

main()