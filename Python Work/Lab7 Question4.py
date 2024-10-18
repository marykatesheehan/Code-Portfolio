#Mary Kate Sheehan
#10/24/2023
#Lab 7 Question 4


pos_count = 0
neg_count = 0
total_count = 0
num_sum = 0


num = int(input("Enter a positive or negative integer (enter 0 to quit program): "))

while num != 0:
    if num > 0:
        pos_count = pos_count + 1
        
    elif num < 0:
        neg_count = neg_count + 1
           
    num_sum = num_sum + num
    total_count = total_count + 1
    num = int(input("Enter a positive or negative integer (enter 0 to quit program): "))
       
average = num_sum // total_count

print("You have inputed", total_count, "numbers. You have inputed", pos_count, "positive numbers and", neg_count, "negative numbers. The average of all the values is", average)
      
    
