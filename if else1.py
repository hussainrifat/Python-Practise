age=int(input("Enter your age: "))
if age>13 and age<18:
    print("You are too young")
    print("Why are you here?")
elif age>30 and age<40:
    print("You are middle age army")
elif age==18:
    print("Perfect! ")
elif age<13:
    print("You are kid")
else:
    print("Hi Grandpa!")
age=None
print("Value of age is now",age)
print(age)