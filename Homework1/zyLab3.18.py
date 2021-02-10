# Kyle Dela Pena
# 2038252

import math

# Dictionary of paint colors and cost per gallon
paint_colors = {'red':35,'blue':25,'green':23}

# FIXME (1): Prompt user to input wall's width
# Calculate and output wall area
height = int(input("Enter wall height (feet):"))
print()
width = int(input("Enter wall width (feet):"))
print()
# FIXME (2): Calculate and output the amount of paint in gallons needed to paint the wall
wall_area = height * width

print("Wall area: " + str(wall_area) + " square feet")


# FIXME (3): Calculate and output the number of 1 gallon cans needed to paint the wall, rounded up to nearest integer
paint_needed = wall_area / 350
cans = math.ceil(paint_needed)

print("Paint needed: {:.2f} gallons".format(paint_needed))
print("Cans needed: " + str(cans) + " can(s)")

# FIXME (4): Calculate and output the total cost of paint can needed depending on color
print()
color = input("Choose a color to paint the wall:")
print()
cost = cans * paint_colors[color.lower()]

print ("Cost of purchasing " + str(color) + " paint: $" + str(cost))
