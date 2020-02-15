
arr = [10, 20, 30, 50, 10, 70, 30]

k = 1
while k < len(arr):

    i = 0
    maxe = 0
    while i+k < len(arr):
        print(arr[ i : k+i ])
        maxe = max( maxe, min(arr[ i : k+i ]) )
        i = i+1
    print('k: ',k, maxe)
    k+=1