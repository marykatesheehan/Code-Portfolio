#Mary Kate Sheehan
#9/27/2023
#Loan qualification exmple: to get loan salary >= 30000, years > 2

salary = eval(input("Enter your salary: "))
years = int(input("Enter number of years of services: "))

if salary >= 30000:
    if years > 2:
        print("You are qualified for the loan.")
    else:
        print("Your salary is good, but the number of years is less than 2.")
        print("You do not qualify for the loan.")
else:
    if years > 2:
        print("Your salary is less than 30000, but the years of service is greater than 2.")
        print("You do not qualify for the loan.")
    else:
        print("Your salary is less than 30000.")
        print("Your years of service is less than 2.")
        print("You do not qualify for the loan.")

print("This is the end of the program.")

    
    
