divisor = int(input("Enter a divisor: "))
list_of_dividends = [12, 65, 72, 39, 108, 339, 221]
def myFunc(x):
    if(x % divisor == 0):
        return( x )
result = list(filter(lambda x : x % divisor == 0,list_of_dividends))
result = list(filter(myFunc,list_of_dividends))
print(result)