a = "Abdul Wasio"
def value():
    a = "Wasio"
    print(a)

def main():
    print(a)
    value()

main()

print(globals()) #globals() is build in pyhton function whihc returns all the global values in the key value pair form means in dictionary form

# We can access specfic global values using globals() function

print(globals()['a'])

# Infact we can change value also

globals()['a'] = "Shaikh"

print(a) #Updated Value