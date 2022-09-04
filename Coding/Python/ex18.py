# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# Ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#this one takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this one takes one arguments
def print_one(arg1):
    print("I got nothin'.")


print_two("Prathyushan","Dinesh")
print_two_again("Prathyushan","Dinesh")
print_one("First!")
print_none() #Let's break down the first function, print_two, which is the most
#similar to what you already know from making.
