
arr2 = [23, 5, 2, 7, 87]
arr1 = [4, 67, 2, 8]

result_arr = []

for x, y in zip(arr1, arr2):

    z = x+y
    if z > 10:
        for i in str(z):
            result_arr.append(i)
    else:
        result_arr.append(z)

if len(arr1) > len(arr2):
    for x in range(len(arr2)+1, len(arr1)+1):
        z = arr1[x-1]
        if z > 10:
            for i in str(z):
                result_arr.append(i)
        else:
            result_arr.append(z)

if len(arr2) > len(arr1):
    for x in range(len(arr1)+1, len(arr2)+1):
        z = arr2[x-1]
        if z > 10:
            for i in str(z):
                result_arr.append(i)
        else:
            result_arr.append(z)

print(result_arr)