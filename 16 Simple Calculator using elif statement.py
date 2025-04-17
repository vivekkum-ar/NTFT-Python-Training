num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

print("Select Operation \n1.Add\n2.Subtract\n3.Multiply\n4.Divide")
operation = input("Enter choice(1/2/3/4):")

if(operation == "1"):
    print("Sum is: ",num1+num2)
elif(operation == "2"):
    print("Difference is: ",num1-num2)
elif(operation == "3"):
    print("Product is: ",num1*num2)
elif(operation == "4"):
    print("Quotient is: ",num1//num2)