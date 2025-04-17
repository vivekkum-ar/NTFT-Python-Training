num = int(input("Enter a number: "))

factorial = 1
for i in range(1,num+1):  # range(1, num+1) is inclusive of num if num is written then it is exclusive of num
    factorial *= i
print("The factorial of", num, "is", factorial)