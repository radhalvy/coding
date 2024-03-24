def get_numbers():

    firstNumber = input("Enter the first number: ")
    if not(firstNumber.isnumeric()):
        get_numbers()
    else:
        secondNumber = input("Enter the second number: ")
        if not(secondNumber.isnumeric()):
            get_numbers()

    return firstNumber, secondNumber

    

def main():
    try:
        operation = int(input("1) Addition, 2) Substraction, 3) Multiplication, 4) Division\n"))
    except:
        print("Invalid operation. Please, try again.")
        main()
    else:
            match operation:
                case 1:
                    num1, num2 = get_numbers()
                    print("The result is:", int(num1) + int(num2))
                    main()
                case 2:
                    num1, num2 = get_numbers()
                    print("The result is:", int(num1) - int(num2))
                    main()
                case 3:
                    num1, num2 = get_numbers()
                    print("The result is:", int(num1) * int(num2))
                    main()
                case 4:
                    num1, num2 = get_numbers()
                    print("The result is:%.2f", int(num1) / int(num2))
                    main()
                case _:
                    print("Invalid operation. Please, try again.")
                    main()

main()