#Mary Kate Sheehan
#10/24/2023
#Lab 7 Question 3

biggest_num = 0
num = int(input("Enter a number (if you wish to stop, enter the number, 0): "))

while num != 0:
    if num > biggest_num:
        biggest_num = num
    num = int(input("Enter a number (if you wish to stop, enter the number, 0): "))
    

print("The biggest number entered was", biggest_num,)
