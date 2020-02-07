
regex = 'ra.*n*.d'
# regex = 'ra.*'
# regex = '.*nd'
# regex = '.*d'

# 'raymonnd'
def apply_regex_on_word(regex, word):





stars = []
for i in range(len(regex)):
    if regex[i] == '*':
        stars.append(i)
print(stars)
matches = []

i=0
for j in stars:
    t = (i, j-1)
    matches.append(t)
    i = i+j+1

t = (stars[len(stars)-1]+1, len(regex)-1)
matches.append(t)
print(matches)

s = 'raymonvjgkkvjhbrtyuiokd'
i=0
repeat = False
for c in s:

    if i >= len(regex):
        print('not matching')
        break

    r = regex[i]
    print(c, r)
    if c == r:
        i+=1
        continue
    elif r == '.':
        i+=1
        continue
    elif r == '*':
        if i+1 < len(regex):
            n = regex[i+1]
            if n == c or n == '.':
                i+=2
            else:
                pass
        else:
            pass
    else:
        print('dont match')
        break
