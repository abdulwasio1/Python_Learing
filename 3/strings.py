name = "Wasio" #Index 0 to n-1 and also -n to -1 (Only in Python)
name1 = 'Wasio'
name2 = '''Waiso'''
print(name , name1 , name2)
print(name[-1]) #print last chararter
sub_string = name1[0:3] # start from 0 till index 2, 3 is exculeded. Output = Was
print(sub_string)

#NEGATIVE SLICING
sub_string2 = name2[-4 : -1] # -1 : -4 reversed negative slicing doesn't work
#-4 : -1 = 1 : 4 get same output
print(sub_string2)

#SLICING TECHNIQUES
print(name[:4]) # 0 to 4
print(name[::-1]) #reverse string
print(name[2:]) # 2 to n-1 where n is length of string
text = "Python Programming"
print(text[::2]) #means 0 to n-1 and :2 means jumps +2
print(text[::-1]) #means reverse string

#SLICING WITH SKIP VALUE
str = "0123456789"
print(str[1:8:3]) # 1:8 means indexes 1 to 7 and :3 means skip values and jump to +3 indexes
#like 1:8 = 1 2 3 4 5 6 7 now jump +3 --> 1 4 7
print(str[1:7:2])
#like 1:7:2 menns 1 2 3 4 5 6 now jumps +2 --> 1 3 5