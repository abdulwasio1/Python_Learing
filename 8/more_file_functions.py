f= open("D:\My Life\Python\data11.txt")
data = f.read()

# f = open("more_data.txt" , 'a') #'a' for append
# data = f.read(10) #Read First 10 Characters 
# data = f.readline() #one line at a time
# data = f.readlines() #all lines as a list (<class 'list'>) Returns list[str]

#LOOPS IN FILE
# for line in f:
#     print(line) #Prints each line that is read from file


# f.writelines(["A\n", "B\n", "C\n"]) #writing multiple lines


# with open("more_data.txt", "r") as f:
#     content = f.read()
# print(content)
#The "with" statement automatically closes the file for you, even if an error occur


print(data)
f.close()


'''
# What happens when mode is 'w' write():
# 1. If file exists → ALL existing content is deleted
# 2. If file doesn't exist → New file is created
# 3. Write pointer starts at BEGINNING

# 'a' mode PRESERVES existing content and adds to end
# What happens:
# 1. If file exists → Content is preserved
# 2. Write pointer starts at END of file
# 3. New data is appended
'''