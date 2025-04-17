a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
max = a
if(b > max):
    max = b
if(c > max):
    max = c

print(max," is the largest number")