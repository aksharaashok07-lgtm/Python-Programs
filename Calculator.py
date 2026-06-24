while True:
    operation = input(
        "\nChoose an operation:\n"
        "a: addition\n"
        "b: subtraction\n"
        "c: multiplication\n"
        "d: division\n"
        "Choice: "
    )

    if operation.lower() == 'a':
        n = int(input("How many numbers do you want to add? "))
        total = 0
        for i in range(n):
            number = float(input(f"Enter number {i+1}: "))
            total += number
        print("The sum is:", total)

    elif operation.lower() == 'b':
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        print("The difference is:", number1 - number2)

    elif operation.lower() == 'c':
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        print("The product is:", number1 * number2)

    elif operation.lower() == 'd':
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        if number2 == 0:
            print("Cannot divide by zero.")
        else:
            print("The quotient is:", number1 / number2)

    else:
        print("Invalid option.")

    again = input("Do you want to perform another calculation? (y/n): ")

    if again.lower() != 'y':
        print("Thank you for using the calculator!")
        print("Bye!")
        break

