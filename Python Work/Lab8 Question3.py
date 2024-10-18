#Mary Kate Sheehan
#10/31/2023
#Lab 8 Question 3

import math

def rectangle_area(length, width):
    area = length * width
    return area

def rectangle_perimeter(length, width):
    perimeter = (length * 2) + (width * 2)
    return perimeter

def circle_area(radius):
    area_of_circle = round(math.pi * (radius ** 2), 2)
    return area_of_circle
 
def circle_circumfrence(radius):
    circumfrence = round(2 * math.pi * radius, 2)
    return circumfrence


def main():
    length = eval(input("Enter the length of your rectangle: "))
    width = eval(input("Enter the width of your rectangle: "))
    radius = eval(input("Enter the radius of your circle: "))

    what_to_display = int(input("Enter the numbers 1 , 2, 3, or 4 (enter 5 to quit): "))
    
    while what_to_display != 5:
        
        if what_to_display == 1:
            print("The area of your rectangle is", rectangle_area(length, width))
            what_to_display = int(input("Enter the numbers 1 , 2, 3, or 4 (enter 5 to quit): "))
            
        elif what_to_display == 2:
            print("The perimeter of your rectangle is", rectangle_perimeter(length, width))
            what_to_display = int(input("Enter the numbers 1 , 2, 3, or 4 (enter 5 to quit): "))
            
        elif what_to_display == 3:
            print("The area of your cirlce is", circle_area(radius))
            what_to_display = int(input("Enter the numbers 1 , 2, 3, or 4 (enter 5 to quit): "))

        elif what_to_display == 4:
            print("The circumfrence of your circle is", circle_circumfrence(radius))
            what_to_display = int(input("Enter the numbers 1 , 2, 3, or 4 (enter 5 to quit): "))

    print("End of program")

main()
                    
    
