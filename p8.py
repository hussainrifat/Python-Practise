import turtle
name=turtle.textinput("name","whats your name")
name=name.lower()
if name.startswith("mr"):
    print("Hello sir How are You?")
elif name.startswith("mrs"):
    print("Hello Madam good morning! ")
else:
    name=name.capitalize()
    n2="Hi"+name+"!"+"how are you"
    print(n2)
turtle.exitonclick()