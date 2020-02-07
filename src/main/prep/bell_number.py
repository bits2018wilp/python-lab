
def bell_number(setn, lst, prev):

    if len(setn) <= 2:
        return

    tmp = list(setn)
    for i in range(len(tmp)):

        t = tmp[i]
        l1 = []
        l1.append(t)
        l2 = tmp[0 : i] + tmp[i+1 : len(tmp)]

        tup=None
        if prev:
            tup = (prev, l1, l2)
        else:
            tup = ( l1, l2)

        lst.append(tup)
        #print(lst)
        bell_number(set(l2), lst, l1)


lst = []
s = set([1, 2, 3, 4])
print(s)
lst.append(set(s))
bell_number(s, lst, None)
c=0
for t in lst:

    print(t)
    tmp = []
    for x in t:
        if isinstance(x, list):
            for y in x:
               tmp.append(y)
        else:
            tmp.append(x)

    b = False
    for i in s:
        if i not in tmp:
            b = True

    if not b:
        c+=1

print(c)

