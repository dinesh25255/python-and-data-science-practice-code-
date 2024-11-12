# Find the  sum of a three digit number  enter by the user  in this program we used in modular


number = int(input('enter a three digit number'))
print(number//10)



a = number % 10

number = number//10

b= number %10
number = number //10

c= number %10


print(a+b+c)