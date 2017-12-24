terminate_program=False
while not terminate_program:
    n1=int(input("Enter a Number: "))
    n2=int(input("Enter another Number "))
    while True:
        operation=input("Please Enter add or sub and quit to exit the program ")
        if operation not in ["add","sub","quit"]:
            print("Unknowm Operation")
            continue
        if operation=="quit":
            terminate_program=True
            break
        if operation=="add":
            print("Addition is ",n1+n2)
        if operation=="sub":
            print("Sub is ",n1-n2)


