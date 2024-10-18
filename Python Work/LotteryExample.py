#Mary Kate Sheehan
#10/18/2023
#Game Lottery Example

import random
num = random.randint(100,999)

guess = int(input("Enter the guess: "))

g_digit1 = guess // 100
g_digit2 = (guess % 100) // 10
g_digit3 = (guess % 100) % 10

num_digit1 = num // 100
num_digit2 = (num % 100) // 10
num_digit3 = (num % 100) % 10

if guess == num:
    print("Match, you won $10,000!")
    
#elif (g_digit1 + g_digit2 + g_digit3 == num_digit1 + num_digit2 + num_digit3):
elif ((g_digit1 == num_digit1 or g_digit1 == num_digit2 or g_digit1 == num_digit3) and
      (g_digit2 == num_digit1 or g_digit2 == num_digit2 or g_digit2 == num_digit3) and
      (g_digit3 == num_digit1 or g_digit3 == num_digit2 or g_digit3 == num_digit3) and
      (g_digit1 != g_digit2) and (g_digit2 != g_digit3) and (g_digit1 != g_digit3)):
    print("Same digits, different order, you won $3,000.")





