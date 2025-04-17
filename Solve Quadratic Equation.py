import cmath

a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

# ------------------------------------------ First root ------------------------------------------ #
x1 = (-b + cmath.sqrt(b**2 -4*a*c))/(2*a)
# ------------------------------------------ Second root ----------------------------------------- #
x2 = (-b - cmath.sqrt(b**2 -4*a*c))/(2*a)

print("the roots are {0} and {1}".format(x1,x2))