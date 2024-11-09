#Q4:- Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input.

import math

# Get the coordinates from the user
x1 = float(input("Enter x-coordinate of the first point: "))
y1 = float(input("Enter y-coordinate of the first point: "))
x2 = float(input("Enter x-coordinate of the second point: "))
y2 = float(input("Enter y-coordinate of the second point: "))

# Calculate the Euclidean distance
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Output the result
print(f"The Euclidean distance between ({x1}, {y1}) and ({x2}, {y2}) is {distance}")
