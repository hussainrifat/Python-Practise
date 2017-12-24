while True:
    n=int(input("Enter a Number "))
    if (n<0):
        print("Enter a Positive Number")
        continue
    if(n==0):
        break
    print("Qube of N is ",n*n*n)