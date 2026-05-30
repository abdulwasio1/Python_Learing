import sys

print(sys.getrecursionlimit()) #Normal recurison limit in py is 1000
sys.setrecursionlimit(20) #but we can change it 
count = 1
def value():
    global count
    print("hello" , count)
    count = count + 1
    #Giving error bcz count is gloabal and count is again local so we are assigning local , global so it is getting confuesd so we can use global keyword to use global
    value()

value()

