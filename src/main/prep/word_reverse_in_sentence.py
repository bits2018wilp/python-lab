
s = 'this is @ #good tests!'
s = 'this/those is @ #good tests!'

arr = []
spl_chars = ['!', '@', '#', '/']

tmp = []
for c in s:
    if c in spl_chars:
        if len(tmp) >0:
            arr.append(''.join(tmp))
            tmp = []
        arr.append(c)
    elif c == ' ':
        if len(tmp) >0:
            arr.append(''.join(tmp))
            tmp = []
    else:
        tmp.append(c)

print(arr)

i = 0
j = len(arr)-1

while i < j:

    while arr[i] in spl_chars:
        i+=1
    while arr[j] in spl_chars:
        j-=1
    if i < j:
        print('swapping ', arr[i], '  ', arr[j], i, j)
        arr[i], arr[j] = arr[j], arr[i]
        print(arr)
    i+=1
    j-=1