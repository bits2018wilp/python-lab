
intervals = [ (1, 2), (3, 5), (6, 7), (8, 10), (12, 16) ]
print(intervals)
n = (4, 9)

new_intervals = []
old_intervals = []

def merge(tuple, intervals):

    m = []
    for i in intervals:

        if i[0] >= tuple[0] and i[1] <= tuple[1]:
            m.append(i)
        elif tuple[0] >= i[0] and tuple[0] <= i[1]:
            m.append(i)
        elif tuple[1] >= i[0] and tuple[1] <= i[1]:
            m.append(i)
    print(m)
    return m

mergeable = merge(n, intervals)

newt = (mergeable[0][0], mergeable[len(mergeable)-1][1])

tmp  = []
tmp.append(newt)
for i in intervals:

    if i not in mergeable:
        tmp.append(i)

tmp.sort(key = lambda  x : x[0])
print(tmp)

for i in intervals:

    if n[0] > i[0] and n[0] < i[1]:
        old_intervals.append(i)
        new_intervals.append((i[0], n[0]))
        new_intervals.append((n[0], i[1]))
        continue

    if n[1] > i[0] and n[1] < i[1]:
        old_intervals.append(i)
        new_intervals.append((i[0], n[1]))
        new_intervals.append((n[1], i[1]))
        continue

tmp = []
for k in range(len(intervals)):
    if intervals[k] not in old_intervals:
        tmp.append(intervals[k])

intervals = tmp
for l in new_intervals:
    intervals.append(l)

print(intervals)

intervals.sort(key = lambda x : x[0])
print(intervals)


