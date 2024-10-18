#Mary Kate Sheehan
#10/10/2023
#Lab5 Question5

mass = eval(input("Enter the indicated mass of an object here in kilograms: "))
weight = mass * 9.8

if weight < 10:
    print("Your object weighs", weight, "newtons. The object is too light!")

if weight > 1000:
    print("Your object weighs", weight, "newtons. The object is too heavy!")

print("End of the program.")
