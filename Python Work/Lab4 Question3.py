#Mary Kate Sheehan
#9/26/2023
#Lab 4 Question 3: Yield the Dollar and Cent Amount from a Floating Price Point

price = eval(input("Enter your floating-point value price here: "))
dollar_amount = int(price)
cents_amount = round(price - dollar_amount, 2)

print("For the price of", price, "dollars, that will yield to,", dollar_amount, "dollars and", cents_amount, "cents.")

