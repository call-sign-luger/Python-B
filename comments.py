'''
This program calculates the area of a 
circle given its radius as input from the user
Formula: A = pi * r^2
'''

# Importing the constant pi from math module
from math import pi

# Taking the radius as input from the user
radius=float(input("Enter the radius of circle: "))

# Calculating the area of circle
area= pi*(radius**2)

# Printing the area of circle
print(f"The area of the circle is {area}")