#Q9:- Given 2 fractions, find the sum of those 2 fractions.Take the numerator and denominator values of the fractions from the user.

import math

# Get input for the first fraction
num1 = int(input("Enter the numerator of the first fraction: "))
den1 = int(input("Enter the denominator of the first fraction: "))

# Get input for the second fraction
num2 = int(input("Enter the numerator of the second fraction: "))
den2 = int(input("Enter the denominator of the second fraction: "))

# Calculate the numerator and denominator of the sum
# Sum of fractions (num1/den1) + (num2/den2) is given by:
# (num1 * den2 + num2 * den1) / (den1 * den2)

sum_num = num1 * den2 + num2 * den1
sum_den = den1 * den2

# Simplify the fraction by finding the greatest common divisor (GCD)
gcd = math.gcd(sum_num, sum_den)
sum_num //= gcd
sum_den //= gcd

# Output the result
print(f"The sum of the two fractions is: {sum_num}/{sum_den}")
