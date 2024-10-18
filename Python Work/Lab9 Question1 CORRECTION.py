)


#CORRECT VERSION

import random
COMPUTER_WINS = 1
PLAYER_WINS = 2
TIE = 0
INVALID = 3
ROCK = 1
PAPER = 2
SCISSORS = 3

def main():
    computer = random.randint(1,3)
    player = int(input("Enter 1 for rock, 2 for paper, 3 for scissors: "))

    print("Computer choice is:", choiceString(computer))
    print("Player choice is:", choiceString(player))

    result = rockPaperScissors(computer, player)

    if result == TIE:
        print("You made the same choice as the computer. Retry!")
    elif result == COMPUTER_WINS:
        print("The computer wins!")
    elif result == PLAYER_WINS:
        print("The player wins!")
        

def rockPaperScissors(computer, player):
    if(computer == player):
        return TIE
    if computer == ROCK:
        if player == PAPER:
            return PLAYER_WINS
        elif player == SCISSORS:
            return COMPUTER_WINS
        else:
            return INVALID
        
    elif computer == PAPER:
        if player == ROCK:
            return COMPUTER_WINS
        elif player == SCISSORS:
            return PLAYER_WINS
        else:
            return INVALID
        
    else: 
        if player == ROCK:
            return PLAYER_WINS
        elif player == PAPER:
            return COMPUTER_WINS
        else:
            return INVALID

def choiceString(choice):
    if choice == ROCK:
        return "rock"
    elif choice == PAPER:
        return "paper"
    elif choice == SCISSORS:
        return "scissors"
    else:
        return "something wrong"
    
        

main()
        



