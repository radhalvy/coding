import random

def get_hand():
    
    userHand = input("Enter your hand: 1) Rock, 2) Paper, 3) Scissors\n")
    
    if (userHand.lower() not in ["rock", "paper", "scissors", "1", "2", "3"]):        
        print("Invalid hand. Please, try again.")
        get_hand()
        
    else:
        return userHand
    
def main():
    
    hands = ("rock", "paper", "scissors")
    userHand = get_hand()
    computerHand = random.choice(hands)
    
    if (userHand == computerHand):        
        print("It's a tie.")
        main()
        
    elif (( (userHand == "rock" or userHand == "1") and computerHand == "paper")
          or ( (userHand == "paper" or userHand == "2") and computerHand == "scissors") 
          or ( (userHand == "scissors" or userHand == "3") and computerHand == "rock") ):
        print("The computer wins.")
        
    else:
        print("You win!")
        
    
main()