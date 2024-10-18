#Mary Kate Sheehan
#10/24/2023
#Lab 7 Question 5

import random
random_number = random.randint(1,100)
guessed_number = int(input("Enter a number between 1 and 100: "))

while random_number != guessed_number:
    if guessed_number > random_number:
        guessed_number = int(input("Too high! Guess the number again: "))
    elif guessed_number < random_number:
        guessed_number = int(input("Too low! Guess the number again: "))

print("Congrats! The number was", guessed_number, "and you guessed correctly!")
