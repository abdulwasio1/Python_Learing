# #Dictionaries are used to store data in key : value or Word : Meaning form
# '''
# What is a Dictionary?
# A dictionary is an unordered, mutable, and indexed collection of key-value pairs. 

# Basic Characteristics :
# Unordered: Items have no fixed position -> No Concpets of Index (Kuch matter nhi krta kio chez phle kio chez bad)
# Mutable: Can be modified after creation
# Indexed by keys: Not by numeric indices like lists
# Keys must be unique (Not Repeatable) and immutable (strings, numbers, tuples)
# Values can be any data type and can be duplicate

# NOTE : "Dictionaries" itself are mutable but inside dictionaries "keys" are immutable 
#         (Possible datatypes : char , str, int, float or tuple)  
# '''
# std_info = {
#     "age" : 18 , #seperated by comma 
#     "name" : "Wasio" ,
#     "Program" : "Computer Science" ,
#     "Marks" : [47.75 , 46.23 , 49.5],
#     's' : ("PF" , "ICT" , "Oops" , "Database"),
#     "is_married" : False
# }

# #NULL DICTIONARY
# null_dict = {} #null dictionary
# print(null_dict)
# null_dict["name"] = "Hello"


# #Values of Dict can be accesed by its "key"
# print(type(std_info))
# print(std_info)
# print(std_info["age"])
# print(std_info["name"])
# print(std_info["Program"])
# print(std_info["Marks"])
# print(std_info["s"])
# print(std_info["is_married"])

# #Modification
# std_info["name"] = "Abdul Waiso" #Update the previous value
# std_info["Caste"] = "Shaikh" #Add new key value pair
# print(std_info)

#NESTED DICTIONARIES
student = {
    "Name" : "Abdul Wasio",

    #Nested

    "Marks" : {
        "Maths" : 97,
        "ICT" : 94,

        #Nested again

        "Programming" : {
            "Python" : 100,
            "C++" : 97,
            "Java" : 96.5
        }
    }
}
# print(student)
# print(student["Marks"])
# print(student["Marks"]["Maths"])
# print(student["Marks"]["Programming"]["Java"])

# #METHODS OF DICTIONARIES

# #1. Print Keys and Values
# print(student.keys())
#    #Typecasting (Tuple into Lists)
# print(list(student.keys()))
# # print(student.values())

# #2. .len, return legth of all keys of Dictionaries
# print(len(student))  #Or we can aslo do that -> print(len(list(student.keys())))

# #3. .items() , return all the (key , val) pairs as tuples
# print(student.items())

# #4. get(), used to get values of particluar key
# print(student.get("Marks")) #return "Marks" keys including all the values inside that key ----> "Better Way" (bcz if a key which does not exists in Dictionary, it will not put error and doesn't affect below down program, it just print NONE)
# print(student["Marks"]) #Get same result above -----> If we access a key that is not present in the Dictionary, this way of accessing will put an error and below down program will not excecute so it is a "Bad Practice"
# # print(student["Marks1"]) #error
# print(student.get("Marks1")) #Print "None. Better way is that Use Methods


#5. .update(), Upadate / Add the keys and Values in Dictionary (Add New Dictionaries)
new_dict = {
    "Name"  : "Wasio Shaikh", #Overwrite previous key with updated values
    "Age" : 19
    # It just add new values if it doesn't exist like age and upadte with new values if already exits like name
}
print(student)
student.update(new_dict) #Itself it return nothing just upadte the value of original Dictionary
print(student)



# ONE MORE INTERSITING THING WE CAN DO WITH DICTINORIES IS COMBINING Keys(sets - unique) and Values(Lists - may or may not)

keys_courses = {'Java' , 'Cpp' , 'Python'}
values_marks = [97.5 , 90.25 , 89.5]
print(type(zip(keys_courses , values_marks))) # --> its class is zip not dictionary we must have to typecast
print(type(dict(zip(keys_courses, values_marks))))
marks_courses = dict(zip(keys_courses, values_marks))
print(marks_courses) #May be order is not maintained (BAD) so we should have to use 'key_courses' as list-
marks_courses.pop("Java") 
del marks_courses["Cpp"] #BOTH removes specfic value 
print(marks_courses)

# Zip is used to combining key and values individually but its type is zip so we must have to typecast it.