
map = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10,
       'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19,
       'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25, 'f':26}

rmap = {}
for k,v in map.items():
    rmap[v]=k

print(map)
print(rmap)

s = '1234'

x = 10

list =[]
dm = ''
for j in range(1,3,1):
    dm = ''
    print(j)
    y = 1
    for i in range(len(s)):
        if j == 1 :
            c = s[y]
            dm = dm + rmap[int(c)]
        else:
            c1 = s[y]

            if i+1 < len(s):
                c2 = s[y+1]
            else:
                c2 = None

            if c2 == None:
                dm = dm + rmap[int(c1)]
            elif int(c1+c2) < 26:
                dm = dm + rmap[int(c1+c2)]
                y = i+1
            else:
                dm = dm + rmap[int(c1)]
        list.append(dm)
print(list)
