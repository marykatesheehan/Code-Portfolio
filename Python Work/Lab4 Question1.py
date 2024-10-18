#MAry Kate Sheehan
#9/26/2023
#Lab 4 Question 1: Find the Subtotal, Sales Tax, and Total with Tax for 5 Items

item1 = eval(input("Enter the price of the first item here: "))
item2 = eval(input("Enter the price of the second item here: "))
item3 = eval(input("Enter the price of the third item here: "))
item4 = eval(input("Enter the price of the fourth item here: "))
item5 = eval(input("Enter the price of the fifth item here: "))

tax = .07

subtotal = item1 + item2 + item3 + item4 + item5
sales_tax = round(((item1 + item2 + item3 + item4 + item5) * tax),2)
total = subtotal + sales_tax

print("The subtotal is", subtotal, "dollars.")
print("The sales tax is", sales_tax, "dollars.")
print("Your total with tax is", total, "dollars.")
