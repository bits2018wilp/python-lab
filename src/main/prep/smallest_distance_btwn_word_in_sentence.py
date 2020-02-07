
s = "world dog cat hello cat dog dog f cat world"

w1 = 'hello'
w2 = 'world'

lst = s.split(" ")
w3 = None
i = 0
j = -1
dist  = 99999
for w in lst:
    j+=1
    print(i, j)
    if w == w1 or w == w2:
        if w3 is None:
            w3 = w
            i = j
        else:
            if w != w3:
                dist = min(dist, j-i)-1
                i=j
            else:
                w3 = w
                i= j
print(dist)
