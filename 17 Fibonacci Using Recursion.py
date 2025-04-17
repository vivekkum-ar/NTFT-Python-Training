num = int(input("Enter a number:"))

a = 0
b = 1
count = 2
print(a, end=" ")
print(b, end=" ")

def fibo(x,y):
    z = x + y
    print(z, end=" ")
    global count
    if(count < num-1):
        count+=1
        fibo(y,z)

fibo(a,b)