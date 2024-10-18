#Mary Kate Sheehan
#10/17/2023
#Lab 6 Question 2

import random
num = random.randint (0,1)
guess = int(input("Enter either you guess of either 0 or 1: "))

if num == guess:
    print("The number randomized was", num, "and you guessed", guess,)
    print("Congrats! You guessed the correct number!")
else:
    print("The number randomized was", num, "and you guessed", guess,)
    print("Sorry! You did not guess the correct number.")

print("End of program.")
