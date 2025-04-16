# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Function to calculate the average of two numbers
def average(x, y):
    return (x + y) / 2

# Main program
def calculator():
    print("Welcome to the Python Calculator!")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Average")

    # Input from the user
    choice = input("Enter choice (1/2/3/4/5): ")

    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"The result of addition is: {add(num1, num2)}")

        elif choice == '2':
            print(f"The result of subtraction is: {subtract(num1, num2)}")

        elif choice == '3':
            print(f"The result of multiplication is: {multiply(num1, num2)}")

        elif choice == '4':
            print(f"The result of division is: {divide(num1, num2)}")

        elif choice == '5':
            print(f"The average is: {average(num1, num2)}")
    else:
        print("Invalid input! Please select a valid operation.")

# Run the calculator
calculator()
