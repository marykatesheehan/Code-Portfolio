#Mary Kate Sheehan
#9/26/2023
#Lab 4 Question 5: Discount Based on Movie Rentals and Movies Referred to new Members

movies_rented = eval(input("Enter the amount of movies rented here: "))
movies_referred = eval(input("Enter the amount of movies referred to new members here: "))

discount = movies_rented + movies_referred

if discount <= 75:
    print("Congrats! You recieve a", discount, "percent discount at the video club!")
else:
    print("You do not recieve a discount at the video club.")



                       
