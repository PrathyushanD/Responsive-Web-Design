# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

#This function subtracts two numbers
def subtract(x, y):
    return x - y


#This function multiplies two numbers
def multiply(x, y):
    return x * y


#This function divides two numbers
def divide(x, y):
    return x / y



print("Select operation.")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

while True:
    #Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    #Chek if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        #Check if the user wants another calculation
        #break the while loop if answer is no
        next_calculation = input("Lets do next calculation? (Y/n): ")
        if next_calculation == "n":
            break

    else:
        print("Invalid Input")
