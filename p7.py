while True:
    n1=input("Enter Your Name: ")
    m=input("Enter Your Question: ")
    if n1.startswith("Mr"):
       print("Dear Sir")
    elif n1.startswith("Mrs"):
        print("Dear Madam")


    if m.endswith("?"):
        print("Thanks For Your Question.We will response soon")
    else: print("Write a Question")

    print("Do You want to Change Your Name?")
    n2=input("Enter Your New Name :")
    n2=n1.replace(n1,n2)
    print("Dear",n2,"Your previous name was",n1,"and You asked",m)



