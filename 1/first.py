# #Q3
# import pyjokes
# print(pyjokes.get_joke()) #generate random jokees(we instal external module of pyjokes using pip keyword --> pip install module_name)

# #Q1

# print('''Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.

# Then the trav'ller in the dark,
# Thanks you for your tiny spark,
# He could not see which way to go,
# If you did not twinkle so.

# In the dark blue sky you keep,
# And often thro' my curtains peep,
# For you never shut your eye,
# Till the sun is in the sky.

# 'Tis your bright and tiny spark,
# Lights the trav'ller in the dark:
# Tho' I know not what you are,
# Twinkle, twinkle, little star.''')
# # we can use triple single code to print as it as output(Multi Lines)
# # we can use triple double code for multi line comments
# # we use hash (#) for single line comment


# #Q4
 
# import os

# # Specify the directory path ('.' refers to the current directory)
# path = '/Sem - 1' #give path with /folder_name
# #simple slash will show all the files and folder in that disk

# # Get a list of all files and folders
# entries = os.listdir(path)

# print(f"Contents of '{path}':")
# for entry in entries:
#     print(entry)

# friend = input("Enter your Name : ").strip().title()
# print(type(friend))
# # age = input("Enter your surname : ")
# # print(name , end="")
# # print(age)
# first, last = friend.split(" ")
# print(f"hello, {first}")


# # Get the user's input
# x = float(input("What's x? "))
# y = float(input("What's y? "))

# # Create a rounded result
# z = round(x + y)

# # Print the formatted result
# print(f"{z:,}")


# HOW TO RoUnd OFF FLOATS USING FORMATTED STRINGS

a = float(input("Enter the Value of a : "))
b = float(input("Enter the Value of b : "))

c = a / b

print(f"{c:.2f}")

