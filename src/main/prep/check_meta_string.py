
s1 = 'geeks'
s2 = 'keegs'

s1 = 'rsting'
s2 = 'string'

if len(s1) != len(s2):
    print('not meta')

c = 0
pi = None
pj = None
found_pair = False
for i, j in zip(s1, s2):

    if i != j:
        c+=1
        if pi is None:
            pi = i
            pj = j
        else:
            if not found_pair and i == pj and j == pi:
                found_pair = True


print(c, found_pair)