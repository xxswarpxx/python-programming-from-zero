def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

while True:
    print("\n--- CALCULATOR ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    option = input("Select an option: ")

    if option == "5":
        print("Program finished.")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if option == "1":
        print("Result:", add(num1, num2))
    elif option == "2":
        print("Result:", subtract(num1, num2))
    elif option == "3":
        print("Result:", multiply(num1, num2))
    elif option == "4":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid option")
