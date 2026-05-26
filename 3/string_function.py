str = "language Model"
print(len(str)) #Count Length of String
print(str.startswith("lan")) #Check whether str start with given text or not -> FALSE
print(str.endswith("uage")) #Check whether str start with given text or not -> TRUE
print(str * 3) #str*str*str like str = "ab" --> ababab

# path = p"\hello"
# print(path)
path = r"C:\Users\Name\Documents"
print(path)  # C:\Users\Name\Documents

print(str.upper()) #Convert String into Upper Case
print(str.lower()) #Convert string into lower case
print(str.swapcase()) #cases are swap Upper -> Lower and Lower -> Upper
print(str.title()) # Capitalize first letter of each word
print(str.capitalize()) #Capitalize first letter of entire String

# Finding substrings
text = "Python is fun and Python is powerful"
print(text.find("Python"))     # 0 (first occurrence)
print(text.rfind("Python"))    # 18 (last occurrence)
print(text.find("Python"))       # -1 (if doesn't not found) 0 (If found)

# Counting occurrences
print(text.count("Python"))    # 2
print(text.count("is"))        # 2

#Replace -> str.replace(old word, new word )
print(text.replace("P" , "CP"))
s = "Helllo Worlld"
print(s.replace("l" , "X" , 2)) #replace first 2 l's with X's
