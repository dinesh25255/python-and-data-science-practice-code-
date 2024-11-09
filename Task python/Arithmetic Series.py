#Q8:- Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series. Assume all inputs are provided by the user.


# Get input from the user
first_term = float(input("Enter the first term of the series: "))
second_term = float(input("Enter the second term of the series: "))
n = int(input("Enter the term position (N) you want to find: "))

# Calculate the common difference
common_difference = second_term - first_term

# Calculate the Nth term using the formula
# Nth term = first_term + (n - 1) * common_difference
nth_term = first_term + (n - 1) * common_difference

# Output the result
print(f"The {n}th term of the series is: {nth_term}")
