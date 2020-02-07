
arr =[1, 2, 3, 4, 5, 6]
k = 3

while k>0:
    i = 0

    while i < len(arr)-1:
        tmp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = tmp
        i+=1
    k-=1
    print(arr)

