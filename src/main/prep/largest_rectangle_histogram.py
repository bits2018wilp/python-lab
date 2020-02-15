
arr = [ 2, 1, 5, 6, 2, 3 ]

leftmin = [None] * len(arr)
rightmin = [None] * len(arr)

print(arr)
area = 0
print(arr)

for i in range(len(arr)):

    t = arr[i] * (len(arr) - i)
    print(arr[i], t)
    if t > area:
        area = t



