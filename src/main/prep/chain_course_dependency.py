
map = {}

map['cs400'] = ['cs500']
map['cs500'] = ['cs200']
map['cs400'] = ['']
map['cs300'] = ['cs100', 'cs200']
map['cs100'] = ['']
map['cs200'] = ['cs100']

# map['cs100'] = ['cs200']
# map['cs200'] = ['cs100']

print(map)

def get_course_path(map):

    tmpstack = []
    for k in map.keys():
        print(k)
        stack = []
        stack.append(k)
        while len(stack) > 0:
            p = stack.pop()
            tmpstack.append(p)
            for v in map[p]:
                if v != '' and v not in stack:
                    if p in map[v]:
                        raise Exception('deadlock...')
                    stack.append(v)

    print(tmpstack)
    courses = []
    while len(tmpstack) > 0:
        p = tmpstack.pop()
        if p not in courses:
            courses.append(p)

    return courses


courses = get_course_path(map)
print(courses)
