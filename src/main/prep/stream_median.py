
import heapq

lo = []
hi = []
last_median = 0

while True:

    a = int(input('enter a number: '))

    if a < last_median:
        heapq.heappush(hi, -1*a)
        heapq.heapify(hi)
    else:
        heapq.heappush(lo, a)
        heapq.heapify(lo)

    if abs(len(hi)- len(lo)) > 1:
        if len(hi) > len(lo):
            p = -1*heapq.heappop(hi)
            heapq.heappush(lo, p)
            heapq.heapify(lo)
            heapq.heapify(hi)
        else:
            p = heapq.heappop(lo)
            heapq.heappush(hi, -1*p)
            heapq.heapify(lo)
            heapq.heapify(hi)

    if len(hi) > len(lo):
        p = -1*heapq.heappop(hi)
        print(p)
        last_median = p
        heapq.heappush(hi, p)
        heapq.heapify(hi)
    elif len(lo) > len(hi):
        p = heapq.heappop(lo)
        print(p)
        last_median = p
        heapq.heappush(lo, p)
        heapq.heapify(lo)
    else:
        p = -1*heapq.heappop(hi)
        heapq.heappush(hi, -1*p)
        heapq.heapify(hi)
        p1 = heapq.heappop(lo)
        heapq.heappush(lo, p1)
        heapq.heapify(lo)
        print( (p+p1)/2 )
        last_median = (p+p1)/2

    print(hi)
    print(lo)