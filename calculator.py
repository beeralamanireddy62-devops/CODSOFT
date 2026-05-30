# Calculator using loop
print("="*40)
print(" SIMPLE CALCULATOR")
print("="*40)

while True:

    # Take input from user
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    # Perform calculation
    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"

    else:
        result = "Invalid operator"

    # Display result
    print("Result =", result)

    # Ask user whether to continue
    choice = input("Do you want to continue? (yes/no): ")

    if choice == "no":
        print("Calculator closed")
        break