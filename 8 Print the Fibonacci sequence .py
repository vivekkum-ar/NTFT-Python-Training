num = int(input("Enter a number: "))

# Print the Fibonacci sequence 

a, b = 0, 1
print("Fibonacci sequence:")
print(a, end=" ")
print(b, end=" ")
for i in range(num - 2):
    # a = b
    # b = a + b 
    a, b = b, a + b # This is a tuple unpacking assignment and same as the above two lines
    print(b, end=" ")
print()  # Print a newline at the end
"""
i | a | b | Printed
- | 0 | 1 | 0 1
0 | 1 | 1 | 1
1 | 1 | 2 | 2
2 | 2 | 3 | 3
3 | 3 | 5 | 5
4 | 5 | 8 | 8
"""