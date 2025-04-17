# ----------------------------- Powers of 2 Using Anonymous Function ----------------------------- #

num = int(input("Enter a number:"))
result = list(map(lambda x: 2 ** x, range(num)))
# x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
# x = lambda a, b : a * b     // OR //    x = lambda a, b, c : a + b + c
for i in range(0,num):
    print("2 raised to power {0} is {1}".format(i,result[i]))