num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

# ----------------------------------------- LCM using GCD ---------------------------------------- #
# -------------------------------- formula is LCM = a.b / gcd(a,b) ------------------------------- #
# min = num1 if num1 < num2 else num2
# gcd = 1  # Initialize gcd with a default value

# while min:
#     if(num1 % min == 0 and num2 % min == 0):
#         gcd = min
#         break  # Exit the loop once gcd is found
#     min -= 1

# print(f"The LCM of {num1} and {num2} is {((num1*num2)/gcd)}")


# ------------------------------------------------------------------------------------------------ #
#                                            Direct LCM                                            #
# ------------------------------------------------------------------------------------------------ #

max = num1 if num1 > num2 else num2 #As LCM cannot be smaller than the larger number
while True:
    if max % num1 == 0 and max % num2 == 0:
        print(f"The LCM of {num1} and {num2} is {max}")
        break
    max += 1
    