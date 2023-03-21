# funtion for addition
def add(a, b):
    return a + b

# function for multiplication
def multiply(a, b):
    return a * b

# function for division
def divide(a, b):
    return a / b

# function for subtraction
def subtract(a, b):
    return a - b

print("Select operation needed")
print("1.Add")
print("2.Multiply")
print("3.Divide")
print("4.Subtract")

while True:
    # get the input from the user
    choice = input("Enter choice (1/2/3/4): ")

    # check if the choice is one of the four choices
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '3':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '4':
            print(num1, "-", num2, "=", subtract(num1, num2))
        break

    else:
        print("Invalid Input")

