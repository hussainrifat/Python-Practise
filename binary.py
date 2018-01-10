l=[12,16,34,65,89]
src=input("Enter Your Item: ")

low = 0
high = 4-1
while low<=high:
    mid=low+high /2
    if l[mid] == src:
        print("Item Found")
        break
    else:

        if l[mid] < src:
        low=mid+1
    else :
        high=mid-1
    mid=(low+high)/2
    if (low>high):
    print("Not Found ")

