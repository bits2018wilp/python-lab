
arr = [1, 16, 4, 7, 10, 11, 7, 12, 6, 7, 19, 18, 2]
#arr = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]

arr = [1, 4, 7, 17, 11, 18, 22, 26, 27, 8, 28]

mmax = arr[0]
pos = []
i = 1

while i < len(arr):
    if arr[i] < mmax:
        i+=1
        pos.append(i-1)

    elif arr[i] > mmax:
        mmax = arr[i]
        i+=1
    else:
        i+=1

print(pos)
mine = min(arr[pos[0] : pos[len(pos)-1]+1])
print(mine)

i = 0
while arr[i] < mine:
    i+=1

j = pos[len(pos)-1]
print(i, j)

print(arr[0:i] + sorted(arr[i:j+1]) + arr[j+1:])