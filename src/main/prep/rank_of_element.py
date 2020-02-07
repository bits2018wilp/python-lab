
arr = [10, 8, 15, 12, 6, 20, 1]

arr2 = arr.copy()
arr2.sort()

print(arr)

for x, y in enumerate(arr2):
    arr[arr.index(y)] = x+1

print(arr)