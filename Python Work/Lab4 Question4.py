#Mary Kate Sheehan
#9/26/2023
#Lab 4 Question 4: Initial Deposite and Interest Rate

initial_deposit = eval(input("Enter your initial deposit into the bank here: "))
monthly_interest = eval(input("Enter your monthly interest percent rate here: "))
monthly_interest = round(monthly_interest / 100, 2)

month_1_total = round((initial_deposit * monthly_interest) + initial_deposit, 2)
month_2_total = round((month_1_total * monthly_interest) + month_1_total, 2)
month_3_total = round((month_2_total * monthly_interest) + month_2_total, 2)

print("After 1 month, you will have", month_1_total, "dollars. After two months, you will have", month_2_total, "dollars. After the third month, you will have", month_3_total, "dollars.")
