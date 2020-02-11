
arr = [1, 5, 3, 4, 6, 8]
ps = sum(arr)//(len(arr)//2)

print(ps)
i= 0
pair = None
j = 0
while len(arr)> 0:

    if not pair:
        pair = arr[i]
    else:
        if ps - pair in arr:
            print(pair, ps-pair)
            arr.remove(pair)
            arr.remove(ps-pair)
            pair = None
            i=0
    i+=1