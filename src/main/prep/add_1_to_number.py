
arr = [9, 8, 9]

bal = 0

for i in range(len(arr)-1, -1, -1):

    x = bal + arr[i]+1

    if x > 9:
        arr[i] = 0
        bal = 1
    else:
        bal= 0
        arr[i] = x

print(bal, arr)
