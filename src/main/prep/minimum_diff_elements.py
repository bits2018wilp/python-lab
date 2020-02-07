
arr1 = [1, 3, 11, 15, 2]
arr2 = [23, 127, 235, 19, 8]

arr = arr1 + arr2
arr.sort()
print(arr1)
print(arr2)
print(arr)

map1 = {}
for i in arr1:
    map1[i] = 1

map2 = {}
for i in arr2:
    map2[i] = 2

i = 0
diff = 99999
p = 0
q = 0
while i < len(arr) - 1:

    if arr[i+1] - arr[i] < diff:

        if arr[i] in map1 and arr[i+1] in map2:
            p = arr[i]
            q = arr[i+1]
            diff = arr[i + 1] - arr[i]
        elif arr[i] in map2 and arr[i+1] in map1:
            p = arr[i]
            q = arr[i+1]
            diff = arr[i + 1] - arr[i]
    i+=1
print(p, q)
