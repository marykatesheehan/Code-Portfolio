#Mary Kate Sheehan
#10/17/2023
#Lab 6 Question 1

num = int(input("Enter a number here: "))

if num % 5 == 0 and num % 6 == 0:
    print("The number is divisible by 5 and 6.")
else:
    print("The number is not divisible by 5 and 6.")
    
if num % 5 == 0 or num % 6 == 0:
    print("The number can be divisible by 5 or 6.")
else:
    print("The number is not divisible by 5 or 6.")

if (num % 5 == 0 or num % 6 == 0) and not (num % 5 == 0 and num % 6 == 0):   
    print("The number is divisible by 5 or 6, but not both.")
else:
    print("The number is not divisible by 5 or 6 and not both.")

print("End of program.")
