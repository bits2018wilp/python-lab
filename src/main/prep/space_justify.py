import math

def char_count(lst):
    total_chars = 0
    for w in lst:
        total_chars = total_chars + len(w)
    return total_chars

words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog", 'and', 'fell', 'shortlyyy']
k = 16

total_lines = math.ceil(char_count(words)/k)
print(total_lines)
i=0
tmp = []
while i < len(words):

    if (char_count(tmp))+len(tmp)-1 < k:
        tmp.append(words[i])
        i+=1

    coount = char_count(tmp) + len(tmp)-1
    #print('ccc', coount, tmp)
    if coount >= k:
        tmp = tmp[0:len(tmp)-1]
        #print(tmp)
        i-=1

        cc = (char_count(tmp))
        spaces = k - cc

        if spaces%(len(tmp)-1) == 0:
            space_list = [' '] * (len(tmp) - 1)
            space_left = spaces - (len(space_list))

            s = 0
            x = 0
            while s < space_left:

                if x == len(space_list):
                    x = 0
                space_list[x] = space_list[x] + ' '
                s += 1
                x += 1

            ttmp = []
            for j in range(len(tmp)):
                ttmp.append(tmp[j])
                if j < (len(space_list)):
                    ttmp.append(space_list[j])
            print(''.join(ttmp))
        else:
            space_list = [' '] * (len(tmp) - 1)
            space_left = spaces - (len(space_list))

            s = 0
            x = 0
            while s < space_left:

                if x == len(space_list):
                    x = 0
                space_list[x] = space_list[x] + ' '
                s += 1
                x += 1

            ttmp = []
            for j in range(len(tmp)):
                ttmp.append(tmp[j])
                if j < (len(space_list)):
                    ttmp.append(space_list[j])
            print(''.join(ttmp))
        tmp = []

if len(tmp) > 0:
    cc = (char_count(tmp))
    spaces = k - cc
    if len(tmp) > 1:
        space_list = [' '] * (len(tmp) - 1)
    else:
        space_list = [' '] * (len(tmp))
    space_left = spaces - (len(space_list))

    s = 0
    x = 0
    while s < space_left:

        if x == len(space_list):
            x = 0
        space_list[x] = space_list[x] + ' '
        s+=1
        x+=1

    ttmp = []
    if len(tmp) == 1:
        ttmp.append(space_list[0])
        ttmp.append(tmp[0])
    else:
        for j in range(len(tmp)):
            ttmp.append(tmp[j])
            if j < (len(space_list)):
                ttmp.append(space_list[j])
    print(''.join(ttmp))
