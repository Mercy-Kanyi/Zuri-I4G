print("Welcome to CLI calculator")

running_prog = True

while running_prog:
    # request type of operator from user
    operator_type = input("Please enter a type of operator: ")
    # prompt user to enter numbers
    try:  # check if number are valid intergers or floats
        first_num = float(input("Enter your first number: "))
        second_num = float(input("Enter your second number: "))
    except:  # if not we print an error message
        print("Failed. Please input valid numbers!")
        continue

    if operator_type == "+":
        print(first_num + second_num)

    elif operator_type == "-":
        print(first_num - second_num)

    elif operator_type == "*":
        print(first_num * second_num)

    elif operator_type == "/":
        print(first_num / second_num)

    elif operator_type == "%":
        print(first_num % second_num)

    else:  # wrong operator
        print("Invalid operator, please try again...")

    new_operation = input("Would you like to try another operation? y/n ")
    if new_operation == "y":
        pass
    elif new_operation == "n":
        running_prog = False
        # same thing as break
print("Thank you for using CLI calculator")
