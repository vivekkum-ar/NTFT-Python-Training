# -------------------------------- Armstrong Number in an Interval ------------------------------- #
# Armstrong numbers are numbers that are equal to the sum of their own digits raised to the power of the number of digits.
# For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.

num = int(input("Enter the lower limit: "))
num2 = int(input("Enter the upper limit: "))

print("Armstrong numbers between", num, "and", num2, "are:")

# ------------------------------------------------------------------------------------------------ #
#                                 Using for and string length logic                                #
# ------------------------------------------------------------------------------------------------ #
for i in range(num, num2 + 1):
    sum = 0
    # Calculate the number of digits in the number
    num_digits = len(str(i))
    # Calculate the sum of the digits raised to the power of num_digits
    for digit in str(i):
        sum += int(digit) ** num_digits
    # Check if the number is an Armstrong number
    if sum == i:
        print(i, end=" ")
        print()  # Print a newline at the end

 # ------------------------------------------------------------------------------------------------ #
 #                                   Using while and divide logic                                   #
 # ------------------------------------------------------------------------------------------------ #

# for num in range(num, num2 + 1):
#     n = len(str(num))
#     result = 0
#     temp = num
#     while temp != 0:
#         remainder = temp % 10
#         result += pow(remainder, n)
#         temp //= 10 # same as temp = temp / 10
#     if result == num:
#         print(num)