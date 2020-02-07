import heapq

arr = [4,6,2,11,8]

heapq.heapify(arr)
print(arr)

for i in range(len(arr)):
    print(heapq.heappop(arr))
