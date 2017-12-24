while True:
    n = int(input("Enter a Number: "))
    if(n<0):
        print("Enter a Positive Number")
        continue
    flag = 0
    for i in range(2, n - 1):
        if (n % i == 0):
            flag = 1
    if (flag == 0):
        print("Prime Number")
    else:
        print("Not Prime")

