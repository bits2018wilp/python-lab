
arr = [4, 3, 6, 2, 4, 2, 3, 4, 3, 3]
arr = [1,3,2,1,4,2]

def  countSetBits_or_pos_for_rightmost_setBit(n):
    count = 0
    i=-1
    loop = True

    while loop:
        i+=1
        count += n & 1
        if count == 1:
            loop = False
        n >>= 1
    return i


res = arr[0]
for i in range(1, len(arr)):
    res = res ^ arr[i]

print(res)
pos = countSetBits_or_pos_for_rightmost_setBit(res)
print(pos)

n = 1
n = n<<pos
print(n)

list1 = []
list2 = []

for x in arr:
    if x & n == 0:
        list1.append(x)
    else:
        list2.append(x)

print(list1)
print(list2)