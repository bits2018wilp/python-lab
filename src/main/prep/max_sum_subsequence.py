
arr = [ 1000, 200, 9, 4, 5, 0, 4, 11, 6]
list = []
list.append(0)

def max_sum2(arr2):

    if len(arr) == 1:
        return arr[0]

    pp =arr[0]
    p = max(arr[0], arr[1])

    for i in range(2, len(arr)):
        curr = max(arr[i], max(p, pp + arr[i]))
        pp = p
        p = curr

    return p

def max_sum(curr_i, sum):

    if curr_i >= len(arr):
        return sum

    sum = sum + arr[curr_i]
    list.append(sum)

    for i in range(curr_i+2, len(arr)):
        max_sum(i, sum)

    return max(list)

print(arr)

cs = 0
ms = 0
list2 = []

# for i in range(len(arr)):
#     ms = max_sum(i, 0)
#     list = []
#     list.append(0)
#     dict = {}
#     list2.append(ms)
#
# print(list2)

x = max_sum2(arr)
print(x)