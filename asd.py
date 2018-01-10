A = [1,3,5,7,11,14,15,20,26,31,44,54,56,80,86]
print(A)
number=int(input("Enter the number:"))
low = 0
high = len(A)-1
while low<= high:
    mid = (low + high) // 2

    if A[mid] == number:
        print('Found')
        break
    else:
        if number> A[mid]:
            low= mid+1
        else:
            high = mid-1
    if low > high:
         print("Not Found")