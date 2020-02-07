
arr = [3, 7, -1, 1]

pos = []

for x in arr:

    if x > 0:
        pos.append(x)

print(pos)

x = 1
for i in range(len(pos)):

    x = pos[i]
    if x < 0:
        x = x*-1

    if x-1 > len(pos)-1:
        continue

    pos[x-1] = -1 * pos[x-1]

for i in range(len(pos)):

    if pos[i] >0:
        print(i+1)
        break