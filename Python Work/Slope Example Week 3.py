#9/20/2023
#Mary Kate Sheehan
#Find the slope of a line passing by two points

x1 = eval(input("Enter x for point 1:"))
y1 = eval(input("Enter x for point 1:"))

x2 = eval(input("Enter x for point 2:"))
y2 = eval(input("Enter x for point 2:"))

#If x1 equals x2 then do not perform the division, instead, tell the user that x2 cannot equal x1
if x1 != x2: #Control the flow
    slope = (y2-y1)/(x2-x1)

    print("The slope of the line passing between the points")
    print("(",x1,",",y1,") and")
    print("(",x2,",",y2,") is")
    print(slope)

else:
    print("You cannot divide by 0. Please enter two new x values")
    x1 = eval(input("Enter x for point 1:"))
    x2 = eval(input("Enter x for point 2:"))

    slope = (y2-y1)/(x2-x1)

    print("The slope of the line passing between the points")
    print("(",x1,",",y1,") and")
    print("(",x2,",",y2,") is")
    print(slope)
    
print("End of the program")
