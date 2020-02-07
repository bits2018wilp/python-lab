
arr = [7,2,3,4,5]

left_prod = [None] * len(arr)
right_prod = [None] * len(arr)

k = len(arr)-1
lp = arr[1]

for i in range(len(arr)):

    if i == 0 :
        left_prod[i] = 1
    else:
        left_prod[i] = arr[i-1] * left_prod[i-1]

    if k ==len(arr)-1:
        right_prod[k] = 1
    else:
        right_prod[k] = arr[k+1] * right_prod[k+1]
    k-=1


prod = [None] * len(arr)
for i in range(len(arr)):
    prod[i] = left_prod[i] * right_prod[i]

print(left_prod, right_prod, prod)