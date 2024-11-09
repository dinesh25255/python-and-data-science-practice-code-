#Q6:- Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.


# Get input from the user
total_heads = int(input("Enter the total number of heads: "))
total_legs = int(input("Enter the total number of legs: "))

# Calculating number of chickens and dogs
# Let chickens = x and dogs = y
# We know:
# x + y = total_heads       (1)
# 2x + 4y = total_legs      (2)

# Solving these two equations:
# From (1): y = total_heads - x
# Substitute y in (2): 2x + 4(total_heads - x) = total_legs

chickens = (4 * total_heads - total_legs) // 2
dogs = total_heads - chickens

# Check if the solution is valid
if chickens >= 0 and dogs >= 0 and (2 * chickens + 4 * dogs) == total_legs:
    print(f"Number of chickens: {chickens}")
    print(f"Number of dogs: {dogs}")
else:
    print("No solution possible with the given heads and legs.")
