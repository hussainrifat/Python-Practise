import random
import math
list=[]
for i in range(5):
    list.append(random.randrange(1,100))

print("Before Sorting: ")
for i in list:
    print(i,end=" ")

print()
i=len(list)-1

while i>1:
    j=0
    while j<i:

        if list[j]>list[j+1]:
            temp=list[j+1]
            list[j]=list[j+1]
            list[j+1]=temp

        j+=1
    i-=1

print("After Sorting: ")
for k in list:
    print(k,end=" ")
