f = open("data.txt" , "r")
# f = open("data.txt" ) #Both are same thing
# Open is Build in Function in python which takes two parameters one is file name nad second is file mode
# Modes means write/read ---> "w"/"r", by default python is on read mode

info = f.read(10) #Read First 10 characters from the file
info = f.read();
print(info)
f.close()

# If we first read entire file using .file() now we are reading again file using readline() then it will print just blank lines bcz pointer
# is shifted to end of file 