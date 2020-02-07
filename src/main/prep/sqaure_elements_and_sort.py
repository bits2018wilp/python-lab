import math

arr = [-9, -2, 0, 2, 3, 10]

i = 0
mine = 99999
for j in range(len(arr)):

    if arr[j] < 0:
        if -1* arr[j] < mine:
            mine = -1*arr[j]
            i = j
    else:
        if arr[j] < mine:
            mine = arr[j]
            i =j

print(i, mine)


l = i-1
r = i+1

arr2 = []
arr2.append(arr[i] * arr[i])

while l >=0 and r < len(arr):

    if (arr[l] * arr[l]) <= (arr[r] * arr[r]):
        arr2.append(arr[l]*arr[l])
        l-=1
    else:
        arr2.append(arr[r] * arr[r])
        r += 1

while l>=0:
    arr2.append(arr[l]* arr[l])
    l-=1

while r < len(arr):
    arr2.append(arr[r] * arr[r])
    r+=1

print(arr2)