
arr = [2,7,4,0,9,5,1,3]
tgt = 6

arr.sort()
print(arr)

s = 0
e = len(arr) -1
i=0
l=0
loop = True

while i < len(arr):

    tmp_tgt = tgt
    tmp_tgt = tmp_tgt - arr[i]

    tmp = arr.copy()

    tmp.remove(arr[i])

    j = 0
    k = len(tmp) -1

    while j < k:

        s = tmp[j] + tmp[k]

        if s == tmp_tgt:
            print(arr[i], tmp[j], tmp[k])
            j+=1
            k-=1

        if s < tmp_tgt:
            j+=1

        if s > tmp_tgt:
            k-=1
    i+=1
