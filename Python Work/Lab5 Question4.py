#Mary Kate Sheehan
#10/10/2023
#Lab5 Question4

length1 = eval(input("Enter your first length of the first rectangle here: "))
width1 = eval(input("Enter your first width of the first rectangle here: "))

length2 = eval(input("Enter your second length of the second rectangle here: "))
width2 = eval(input("Enter your second width of the second rectangle here: "))

area1 = length1 * width1
area2 = length2 * width2

if area1 > area2:
    print("The first rectangle has the greater area of", area1, "while the second rectangle has the lesser area of", area2)

if area2 > area1:
    print("The second rectangle has the greater area of", area2, "while the first rectangle has the lesser area of", area1)

print("End of the program.")


    
