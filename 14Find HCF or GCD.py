num1 = int(input("Enter First number:"))
num2 = int(input("Enter Second number:"))
min_val = num1 if num1 < num2 else num2  # as GCD cannot be greater than the smallest number

# ------------------------------------------- Using For ------------------------------------------ #

# for i in range(1, min_val + 1):
#     if(num1 % i == 0 and num2 % i == 0):
#         gcd = i
# print(f"GCD of {num1} and {num2} is {gcd}")

# ------------------------------------------ Using While ----------------------------------------- #

while min_val:
    if(num1 % min_val == 0 and num2 % min_val == 0):
        gcd = min_val
        break
    min_val-=1  #Decrease continuousely so while can continue or while will run for infinite time
print(f"GCD of {num1} and {num2} is {gcd}")