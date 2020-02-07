
import heapq

class StackElement:

    def __init__(self, val, counter):

        self.val = val
        self.counter = counter

    def __lt__(self, other):
        return other.counter < self.counter

    def __str__(self):
        return str(self.val) + ", " + str(self.counter)

arr = []
i=0
heapq.heappush(arr, StackElement(2, i))
i+=1
heapq.heappush(arr, StackElement(3, i))
i+=1
heapq.heappush(arr, StackElement(1, i))

heapq.heapify(arr)

print(heapq.heappop(arr))
