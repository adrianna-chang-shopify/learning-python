# Learning about functions in Python!

# Testing out the raw_input function
a = raw_input("Type in something, and it will be repeated on the screen: ")
# print value of a
print a

#Calculator Program

def menu():
    #print what options you have
    print ""
    print "Your options are:"
    print " "
    print "1) Addition"
    print "2) Subtraction"

    print "3) Multiplication"

    print "4) Division"
    print "5) Quit program"
    print " "
    return input("Choose your option: ")

def add(val1, val2):
    print val1, "+", val2, "=", val1 + val2

def subtract(val1, val2):
    print val1, "-", val2, "=", val1 - val2

def multiply(val1, val2):
    print val1, "*", val2, "=", val1 * val2

def divide(val1, val2):
    print val1, "/", val2, "=", val1 / val2

loop = 1 # start loop at 1 so menu runs
choice = 0 # choice for the user

print "Welcome to Adrianna's calculator program!"

while loop == 1:
    choice = menu()
    if choice == 1:
        add(input("Value 1: "), input("Value 2: "))
    elif choice == 2:
        subtract(input("Value 1: "), input("Value 2: "))
    elif choice == 3:
        multiply(input("Value 1: "), input("Value 2: "))
    elif choice == 4:
        divide(input("Value 1: "), input("Value 2: "))
    elif choice == 5:
        loop = 0
	
print "Goodbye!"
