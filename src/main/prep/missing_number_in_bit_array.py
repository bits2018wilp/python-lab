import math

arr = [ [1, 1], [0, 1], [0, 0] ]

# missing, [1,1,0]
# 00, 01, 10, 11
# (n*(n+1))/2

n = 3
ts = (n *(n+1))//2
s = 0
for i in range(0, len(arr)):

    tmp = arr[i]
    t = 0
    k=0
    for j in range( len(tmp)-1, -1, -1):
        #print('j: ', j, tmp[j], math.pow(2, k))
        t = t + ( (tmp[j]) * (math.pow(2, k)))
        k+=1
    s = s+t
print(tmp, t, s, 'missing: ', ts-s)

