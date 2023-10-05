# Add Function
def add(x, y):
    return x + y

# Subtract Function
def subtract(x, y):
    return x - y

# Multiply Function
def multiply(x, y):
    return x * y

# Divide Function
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero."
    return x / y

# Asking user to select operation
print("Select Operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

# Checking if the choice is valid
if choice in ['1', '2', '3', '4']:

    # Taking numbers from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
else:
    print("Invalid Input")
