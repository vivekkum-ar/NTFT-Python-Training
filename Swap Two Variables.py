# This code takes two numbers as input and swaps them without using a temporary variable.
x = int(input("Enter first number:"))
y = int(input("Enter second number:"))

# x = x + y
# y = x - y
# x = x - y

x = x*y
y = x/y
x = x/y
print("After swapping, first number is {0} and second number is {1}".format(x, y))