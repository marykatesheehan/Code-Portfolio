#Mary Kate Sheehan
#10/24/2023
#Lab 7 Question 2


#FOR LOOP

num = int(input("Enter a non-negative number: "))
value = 1

for value in range(1,num + 1):
    factorial = num % value
    if factorial == 0:
        print(value)

print("Above, these are all the factorials that go into", num) 


#WHILE LOOP

num = int(input("Enter a non-negative number: "))
value = 1

while value <= num:
    factorial = num % value
    if factorial == 0:
        print(value)
    value = value + 1

print("Above, these are all the factorials that go into", num)

 
    
    
