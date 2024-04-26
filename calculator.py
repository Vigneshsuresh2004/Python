def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero!"

def calculator(operator, x, y):
    switcher = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    # Get the function from switcher dictionary
    func = switcher.get(operator)
    # Execute the function
    if func:
        return func(x, y)
    else:
        return "Invalid operator"

# Test the calculator
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = None
if choice in ['1', '2', '3', '4']:
    if choice == '1':
        result = calculator('add', num1, num2)
    elif choice == '2':
        result = calculator('subtract', num1, num2)
    elif choice == '3':
        result = calculator('multiply', num1, num2)
    elif choice == '4':
        result = calculator('divide', num1, num2)
    print("Result:", result)
else:
    print("Invalid input")
