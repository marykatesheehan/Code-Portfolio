#Mary Kate Sheehan
#11/7/2023
#Lab 9 Question 3

import random

num1 = random.randint(0, 1000)
num2 = random.randint(0, 1000)

print("What is", num1, "+", num2)
computer_answer = num1 + num2
user_answer = int(input("Enter answer here : "))

if user_answer == computer_answer:
    print("The answer was", computer_answer, "and you got it CORRECT!")

else:
    print("The answer was", computer_answer, "and you got it WRONG!")



