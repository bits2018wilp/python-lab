
map = {}

map['d'] = ['a', 'b']
map['b'] = ['f']
map['a'] = ['f']
map['c'] = ['d']


stack = []
visited = []
path = []
stack.append('d')

while len(stack) > 0:

    print(stack)
    p = stack.pop()
    d = map.get(p)

    if d is None or len(d) == 0:
        if p not in path:
            path.append(p)
        visited.append(p)
        continue
    else:
        if p not in visited:
            stack.append(p)
            visited.append(p)
        else:
            if p not in path:
                path.append(p)

    for c in d:
        if c not in visited:
            stack.append(c)

prj = ['a', 'b', 'c', 'd', 'e', 'f']
print(path)
for p in prj:
    if p not in path:
        path.append(p)
print(path)