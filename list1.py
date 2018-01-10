import random
import math
randlist=["String",3.2323,3,"String"]
onetoten=list(range(10))
randlist=randlist+onetoten
print(onetoten)
print()
print(randlist)
print()
print(len(randlist))
print()
first2=randlist[0:2]
print("First 2 Number:",first2)
print()
first4=randlist[0:4]
print("First 4 Number:",first4)
#printing first 4 number
print()
for i in first4:
    print("{}:{}".format(first4.index(i),i))
print()
    #printing first 3 number with index

for i in first2:
    print("{}:{}".format(first2.index(i),i))

print()
print("String" in first2)
print(3 in first4)
print("How many string:",first4.count("String"))

