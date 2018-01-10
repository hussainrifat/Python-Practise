list=[12,23,54,57,34,65,75,42 ]

i=len(list)-1
while i>1:
    j=0
    while j<i:
          print("\nIs {} > {}".format(list[j],list[j+1]))
        if list[j]>list[j+1]:

            print("Switch")

            temp=list[j+1]
            list[j]=list[j+1]
            list[j+1]=temp

        else:

            print("Dont Switch")

        j+=1
        for k in list:
            print(k, end=" ")
            print()

    i-=1

print()
print("After Sorting: ")
for k in list:
    print(k,end=" ")