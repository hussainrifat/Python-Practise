def add(a,b):
    return a+b
while True:
    n=int(input("Enter Number 1: "))
    m=int(input("Enter Number 2: "))
    if (n<0 and m<0):
        break
    result=add(n,m)
    print(result)