#Mary Kate Sheehan
#10/17/2023
#Lab 6 Question 5

savings_balance = eval(input("Enter the initial balance of the savings account: "))
if savings_balance < 0:
    savings_balance = eval(input("Your savings cannot start in the negatives. Enter a new initial balance of the savings account: "))

checking_balance = eval(input("Enter the initial balance of the checking account: "))
if checking_balance < 0:
    checking_balance = eval(input("Your checking cannot start in the negatives. Enter a new initial balance of the checking account: "))
    

userTransaction = input("Are you tring to deposit, withdraw, or transfer money?")

if userTransaction == "deposit":
    checking_or_savings = input("Are you depositing into checking or savings?")
    if checking_or_savings == "checking":
        deposit_value = eval(input("Enter number how much money you are depositing: "))
        checking_balance = checking_balance + deposit_value
    elif checking_or_savings == "savings":
         deposit_value = eval(input("Enter number how much money you are depositing: "))
         savings_balance = savings_balance + deposit_value


if userTransaction == "withdraw":
    checking_or_savings = input("Are you withdrawing from checking or savings?")
    if checking_or_savings == "checking":
        withdraw_value = eval(input("Enter number how much money you are withdrawing: "))
        if withdraw_value > checking_balance:
            withdraw_value = eval(input("Too big of a withdraw! Enter number how much money you are withdrawing: "))
            checking_balance = checking_balance - withdraw_value
        else:
            checking_balance = checking_balance - withdraw_value    
    elif checking_or_savings == "savings":
         withdraw_value = eval(input("Enter number how much money you are withdrawing: "))
         if withdraw_value > savings_balance:
            withdraw_value = eval(input("Too big of a withdraw! Enter number how much money you are withdrawing: "))
            savings_balance = savings_balance - withdraw_value
         else:
            savings_balance = savings_balance - withdraw_value


if userTransaction == "transfer":
    checking_or_savings = input("Are you transfering money from checking or savings?")
    if checking_or_savings == "checking":
        transfer_value = eval(input("Enter number how much money you are transfering to your savings: "))
        if transfer_value > checking_balance:
            transfer_value = eval(input("Too big of a withdraw! Enter number how much money you are transfering: "))
            checking_balance = checking_balance - transfer_value
            savings_balance = savings_balance + transfer_value
        else:
            checking_balance = checking_balance - transfer_value
            savings_balance = savings_balance + transfer_value
    if checking_or_savings == "savings":
        transfer_value = eval(input("Enter number how much money you are transfering to your savings: "))
        if transfer_value > savings_balance:
            transfer_value = eval(input("Too big of a withdraw! Enter number how much money you are transfering: "))
            checking_balance = checking_balance + transfer_value
            savings_balance = savings_balance - transfer_value
        else:
            checking_balance = checking_balance + transfer_value
            savings_balance = savings_balance - transfer_value

print("You now have the balance in your checking account of", checking_balance)
print("You now have the balance in your savings account of", savings_balance)
            

    

    
    
