#Mary Kate Sheehan
#11/7/2023
#Lab 9 Question 1

import random

computer_answer = random.randint(1, 3)
    
if computer_answer == 1:
    computer_answer = "rock"
        
elif computer_answer == 2:
    computer_answer = "paper"

elif computer_answer == 3:
    computer_answer == "scissors"

user_answer = input("Enter rock, paper, or scissors: ")

if computer_answer == user_answer:
    print("There was a tie! The computer picked", computer_answer, "and you picked", user_answer)


if computer_answer == "rock" and user_answer == "paper":
    print("You win! You chose", user_answer, "while the computer chose", computer_answer)

elif computer_answer == "scissors" and user_answer == "rock":
    print("You win! You chose", user_answer, "while the computer chose", computer_answer)

elif computer_answer == "paper" and user_answer == "rock":
    print("You lose! You chose", user_answer, "while the computer chose", computer_answer)

elif computer_answer == "rock" and user_answer == "scissors":
    print("You lose! You chose", user_answer, "while the computer chose", computer_answer)

elif computer_answer == "paper" and user_answer == "scissors":
    print("You win! You chose", user_answer, "while the computer chose", computer_answer)

elif computer_answer == "scissors" and user_answer == "paper":
    print("You win! You chose", user_answer, "while the computer chose", computer_answer)
