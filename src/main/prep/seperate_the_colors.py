
arr = ['G', 'B', 'R', 'R', 'B', 'R', 'G']

r = 0
g = 0
b = 0

i = 0
e = len(arr)-1
s = 0

while i < len(arr):
    print(arr,i, s, e)
    if arr[i] == 'R':
        t = arr[i]
        arr[i] = arr[s]
        arr[s] = t
        i+=1
        s+=1
    elif arr[i] == 'G':
        t = arr[i]
        arr[i] = arr[e]
        arr[e] = t
        e-=1
    else:
        i+=1

print(arr)
