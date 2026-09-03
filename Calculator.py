def calculator():
    print("Welcome to the Calculator!")

    while True:
        try:
            n1 = float(input("Enter the first number: "))
        except ValueError:
            print("Error: Invalid input. Please enter a number.")
            continue
        
        operation = input("Enter an operation: ")
        if operation not in ["+", "-", "*", "/","%","**"]:
            print("Error: Invalid operation. Please enter one of +, -, *, /,%,**.")
            continue

        try:
            n2 = float(input("Enter the second number: "))
        except ValueError:
            print("Error: Invalid input. Please enter a number.")
            continue

        try:
            if operation == "+":
                result = n1 + n2
            elif operation == "-":
                result = n1 - n2
            elif operation == "*":
                result = n1 * n2
            elif operation == "/":
                result = n1 / n2
            elif operation == "%":
                result = n1 % n2
            elif operation == "**":
                result = n1 ** n2
            else:
                print("Error: Unknown operation.")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
            continue

        print(f"{n1} {operation} {n2} = {result}")

        again = input("Do you want to perform another calculation? (yes/no): ")
        if again == "y" or again == "yes":
            continue
        elif again == "n" or again == "no":
            print("Thank you for using the calculator. Goodbye!")
            break
        else:
            print("Invalid input. Exiting the calculator.")

calculator()