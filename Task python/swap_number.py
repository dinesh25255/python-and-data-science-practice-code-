#Q3:- Take 2 numbers as input from the user.Write a program to swap the numbers without using any special python syntax.

# Input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(f"Before swapping: num1 = {num1}, num2 = {num2}")

# Swapping without using special syntax
temp = num1
num1 = num2
num2 = temp

print(f"After swapping: num1 = {num1}, num2 = {num2}")