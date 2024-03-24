import random

randomNumber = random.randint(0, 10)

def get_user_number():    
    userNumber = input("Enter your guess: ").lower()
    if not userNumber.isnumeric():
        print("Invalid guess. Please, try again.")
        main()
    else:
        return int(userNumber)
    
    
def main():
    userNumber = get_user_number()
    if userNumber == randomNumber:
        print("You guessed right!")
    elif userNumber < randomNumber:
        print("Higher")
        main()
    else:
        print("Lower")
        main()
        
        
main()