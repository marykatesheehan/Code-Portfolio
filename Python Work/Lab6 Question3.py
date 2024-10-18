#Mary Kate Sheehan
#10/17/2023
#Lab 6 Question 3

import random

num = random.randint(100,999)
numD3 = num % 10
numD2 = (num //110) % 10
numD1 = num // 100

guess = int(input("Enter a three-digit number: "))
guessD3 = guess % 10
guessD2 = (guess //110) % 10
guessD1 = guess // 100

print("The number is", num)

if num == guess:
    print("You won $10,000.")

elif num == int(guessD1 + guessD2 + guessD3) or num == int(guessD2 + guessD1 + guessD3) or num == int(guessD2 + guessD3 + guessD1) or num == int(guessD3 + guessD1 + guessD2) or num == int(guessD3 + guessD2 + guessD1):
        print("You won $3,000.")

elif numD1 == guessD1 or numD1 == guessD2 or numD1 == guessD3:
        print("You won $1,000.")
        
elif numD2 == guessD1 or numD2 == guessD2 or numD3 == guessD3:
        print("You won $1,000.")
        
elif numD3 == guessD1 or numD3 == guessD2 or numD3 == guessD3:
        print("You won $1,000.")
        
else:
    print("You have lost. Sorry!")



