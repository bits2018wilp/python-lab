
s = 'justcheckuniquechars'

s = sorted(s)
print(s)

prev = None
for c in s:

    if c == prev:
        print('dupe chars')
        break
    else:
        prev = c
