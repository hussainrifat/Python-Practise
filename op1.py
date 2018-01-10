

while True:
    num1, op, num2 = input("Enter Number: ").split()
    num1 = int(num1)
    num2 = int(num2)


    if op == "+":
        print("Addition is ", num1 + num2)
    elif op == "-":
        print("Substraction is ", num1 - num2)
    elif op == "*":
        print("Multipliction is ", num1 * num2)
    elif op == "-":
        print("Divide is ", num1 - num2)
    else:
        print("Unknown Operator")