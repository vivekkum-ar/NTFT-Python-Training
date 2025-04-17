num = int(input("Enter a number:"))
sum = 0
for i in range(num+1):
    sum += i
print("Sum from 1 to {0} is {1}".format(num,sum))