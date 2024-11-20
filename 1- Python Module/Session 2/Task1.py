# Write a Python program which accepts the radius of a circle 
# from the user and compute the area?

import math

radius=int(input("Enter the Circle radius"))
area = math.pi * (radius**2)

print(f"The Area of the Circle of radius {radius} is {area}")