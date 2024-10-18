#Mary Kate Sheehan
#9/18/2023
#Radius to Circumfrance, Area, Volume, and Surface Area

import math
radius = eval(input("Enter the radius here: "))
area = round(math.pi * radius**2, 2)
circumfrence = round(2 * math.pi * radius, 2)
volume = round(4/3 * math.pi * radius**3, 2)
surface_area = round(4 * math.pi * radius**2, 2)
print("The area of the circle is", area)
print("The circumfrence of the circle is", circumfrence)
print("The volume of the sphere is", volume)
print("The surface area of the sphere is", surface_area)
