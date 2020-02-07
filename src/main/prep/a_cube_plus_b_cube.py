import math
n = 50

map = {}

for i in range(1, n+1):
    for j in range(1, n+1):

        result = math.pow(i, 3) + math.pow(j, 3)
        if result in map.keys():
            l = map[result]
            l.append((i, j))
        else:
            map[result] = [(i, j)]

print(math.pow(1,3) + math.pow(12,3), math.pow(9,3)+ math.pow(10, 3))
for k, v in map.items():

    if len(v) > 2:
        print(v)
