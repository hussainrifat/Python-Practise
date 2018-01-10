
for i in range(1,101):
    if (i%3==0) and (i%5==0) :
        print(i,"is Fizzbuzz")
    elif (i%3==0):
        print(i,"is Fiz")
    elif (i%5==0):
        print(i,"is Buzz")
    else:print(i)