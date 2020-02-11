
arr = [1, 5, 3, 5, 5, 5,4,7]

#arr = [9, 2, 5, 9, 5, 9, 5, 9, 5, 9]

maj_index = 0
count = 1

for j in range(1, len(arr)):

    if arr[j] == arr[maj_index]:
        count+=1
    else:
        count-=1

    if count <=0:

        maj_index = j
        count = 1

print(maj_index)
count=0
for x in arr:

    if x == arr[maj_index]:
        count+=1

if count >= len(arr)//2:
    print(arr[maj_index])
else:
    print('no major element')