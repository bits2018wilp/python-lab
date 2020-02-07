
arr =[1,2,3,4,5]
k =9

i = 1
j = 0
while i < len(arr):

    print(i, j, arr[i:j])
    if sum(arr[j:i]) == k:
        print(i, j, arr[j:i])
        break
    elif sum(arr[j:i]) > k:
        j+=1
    else:
        i+=1

