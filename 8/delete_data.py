import os 
# Using os module
# Module (like a code library) is a file written by another programmer that generally has a functions we can use
with open("file_data_detele.txt" , 'w+') as f:
    f.write("Hello this is me Abdul Wasio Shaikh")
    f.seek(0)
    data = f.read()
os.remove("file_data_detele.txt") #Not only data is deleted, entire file is deleted (File doesn't exist in memory)
print(data)
