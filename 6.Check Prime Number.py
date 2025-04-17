# The above code checks if a number is prime or not.
num = int(input("Enter a number: "))


# ------------------------------------------ FOR REVERSE ----------------------------------------- #
# range(10, 2) is empty → []
# range(10, 2, -1) → [10, 9, 8, 7, 6, 5, 4, 3] ✅ works in reverse


for i in range(num-1, 2, -1): # we can also use for i in range(2, num-1):
    if num % i == 0:
        print(num, "is not a prime number")
        break
else:
    print(num, "is a prime number")