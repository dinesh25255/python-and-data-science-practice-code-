### Q5:- Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user.
#


# Get input from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time period (in years): "))

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

# Output the result
print(f"The simple interest is: {simple_interest}")
