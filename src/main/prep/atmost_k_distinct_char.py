
s = 'abcba'
k = 2

lst= []

bool = True
i=0

def distinct_char(lst):
    c=0

    tmp = []
    for x in lst:
        if x not in tmp:
            tmp.append(x)
            c+=1
    return c

print(distinct_char(['b','c','b']))

flst = []
lst = []

while i < len(s):

    lst.append(s[i])

    if distinct_char(lst) == k:
        flst.append(lst.copy())

    if distinct_char(lst) > k:
        lst = lst[1:]

    if distinct_char(lst) == k:
        flst.append(lst.copy())

    i+=1

print(flst)
