
arr = [34, 8, 10, 3, 2, 80, 30, 33, 1]
print(arr)

arrs = arr.copy()

stack1 = []
stack2 = []
map = {}

for i, x in enumerate(arr):
   map[x] = i

arrs.sort()
print(arrs)
print(map)

n = len(arr)
maxdiff = 0
temp = n

for i in arrs:

    if map[i] < temp:
        temp = map[i]
    maxdiff = max(maxdiff, (map[i] - temp))

print(maxdiff)