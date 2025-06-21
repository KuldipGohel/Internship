def calculator():
    print("Simple_Calculator")

    while True:
        try:
            num1 = float(input("\nEnter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if operator == '+':
                print("Addition is:", num1 + num2)
            elif operator == '-':
                print("Subtraction is:", num1 - num2)
            elif operator == '*':
                print("Multiplication is:", num1 * num2)
            elif operator == '/':
                if num2 != 0:
                    print("Division is:", num1 / num2)
                else:
                    print("You Can't Divide By Zero!!")
            else:
                print("You Entered Invalid Operator")

        except ValueError:
            print("Invalid input! Please enter numbers only...")

        choice = input("\nDo you want to perform another operation? (Yes/No): ")
        if choice.lower() != 'yes':
            print("Have A Nice Day!")
            break

calculator()
