def get_numbers():

    firstNumber = input("Enter the first number: ")
    if not(firstNumber.isnumeric()):
        main()
    else:
        secondNumber = input("Enter the second number: ")
        if not(secondNumber.isnumeric()):
            main()
        else:
            return int(firstNumber), int(secondNumber)

def get_operation():
    
    operation = input("1) Addition, 2) Substraction, 3) Multiplication, 4) Division\n")
    if not operation.isnumeric():
        print("Invalid operation. Please, try again.")
        main()
    else:
        return int(operation)

    

def main():
    
    operation = get_operation()
    match operation:
        case 1:
            num1, num2 = get_numbers()
            print("The result is:", num1 + num2)
            main()
        case 2:
            num1, num2 = get_numbers()
            print("The result is:", num1 - num2)
            main()
        case 3:
            num1, num2 = get_numbers()
            print("The result is:", num1 * num2)
            main()
        case 4:
            num1, num2 = get_numbers()
            print("The result is:", num1 / num2)
            main()
        case _:
            print("Invalid operation. Please, try again.")
            main()

main()