# f = open("filemodes.txt" , "r+")
# data = f.write("Your data is Overwriten")
# print(f.read())
# f.close()

'''
FLOW OF FILE
1. If data is already written in file then that data is overwriten by provided data bcz r+ moded sets pointer in the begining of file
2. Now after that we are reading file now as we know our file pointer is at the end of above provided text
   like if I write "abcdef" now file pointer is just after character 'f', " so text after the pointer is printed"

if we Open file in w+ modes then file open in trucated mode means entire data is erased first then if we write, we can
 

# '''
# f =open("filemodes.txt" , 'a+' ) #file is opened and then truncated
# data = f.read()
# print(data) #Nothing is printed bcz file is opened in truncated mode
# f.write("Previous data is truncated and new data is written")
# data = f.read() #Now after writting pointer is at the end of file so it will read nothing
# print(data)

'''
After writing, the file pointer is positioned at the end of the file. When you call read() from the end position, there's nothing left to read.

SOLUTION
'''
# f = open("filemodes.txt", "w+")
with open("filemodes.txt" , 'w+') as f:
   f.write("Previous data is truncated and new data is written")
   f.seek(0)  # Move file pointer to beginning of file to read data from starting
   data = f.read()
   print(data)  # Now it prints: "Previous data is truncated and new data is written"
   f.close()



''''
r  Read-only. Raises I/O error if file doesn't exist.
r+	Read and write. Raises I/O error if the file does not exist.
w	Write-only. Overwrites file if it exists, else creates a new one.
w+	Read and write. Overwrites file or creates new one and pointer is at end.
a	Append-only. Intially Pointer is at the end of file.Adds data to end. Creates file if it doesn't exist.
a+	Read and append. Pointer at end. Creates file if it doesn't exist.
'''