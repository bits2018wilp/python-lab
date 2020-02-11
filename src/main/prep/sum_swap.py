
arr1 = [4,1,2,1,1,2]
sum1 = sum(arr1)

arr2 = [3,6,3,3]
sum2 = sum(arr2)


arr1 = [3, 6, 7, 1,0]
sum1 = sum(arr1)

arr2 = [4, 7, 2, 5, 1]
sum2 = sum(arr2)

avg_sum = (sum1+sum2)//2

print(sum1, sum2, avg_sum)

d = sum2 - avg_sum
i = 0
dd = 999
l = 0

while i < len(arr2):
    if arr2[i] >= d and arr2[i] - d < dd:
        dd = arr2[i] - d
        l = arr2[i]
    i+=1

print(l, l-d)
