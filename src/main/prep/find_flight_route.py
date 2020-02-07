
arr = [ ('A', 'B'), ('A', 'C'), ('B', 'C'), ('C','A') ]
arr = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
start = 'YUL'

dict = {}

for t in arr:

    o = t[0]
    d = t[1]
    if o in dict:
        l = dict[o]
        l.append(d)
        dict[o] = l
    else:
        l = []
        l.append(d)
        dict[o] = l

print(dict)
path = []

while len(dict) >0:
    path.append(start)
    l = dict[start]
    if len(l) > 1:
        l.sort()
    p = start
    start = l[0]
    l.remove(start)
    if len(l) == 0:
        del dict[p]
path.append(start)
print(path)