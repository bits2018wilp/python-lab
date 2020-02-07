
arr = [10, 2, 8, 4, 3]

i = 1

while i < len(arr):

    if arr[i] < arr[i-1] and i+1 < len(arr) and arr[i] < arr[i+1]:
        avg = (arr[i-1]+ arr[i+1])//2
        if avg < arr[i-1] and avg > arr[i+1]:
            arr[i] = avg
        else:
            print('false')
            break

    i+=1

print(arr)