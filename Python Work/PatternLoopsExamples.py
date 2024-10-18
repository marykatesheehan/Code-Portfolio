#Mary Kate Sheehan
#10/23/2023
#Displaying patterns using nested loops in Python


#EXAMPLE 1: Display a Rectangle

for row in range(8):
    for column in range(6):
        print("*", end = "") #can change the "*" to any symbol of your choosing
    print()

#output:
    # ********
    # ********
    # ********
    # ********
    # ********
    # ********
    

#EXAMPLE 2: Using Variables to Display Rectangle

width = int(input("Enter width of rectangle: "))
length = int(input("Enter length of rectangle: "))

for row in range(length):
    for column in range(width):
        print("*", end = "")
    print()
 

#EXAMPLE 3: Display a Triangle

for r in range(5):
    for c in range(r+1):
        print("*", end = "")
    print()

#output:
    # *
    # **
    # ***
    # ****
    # *****
    

    
#EXAMPLE 4: Display Stairs

num_steps = 5

for r in range(num_steps):
    for c in range(r):
        print(" ", end="")
    print("*")
    
#output:
    # *
    #  *
    #   *
    #    *
    #     *
    

