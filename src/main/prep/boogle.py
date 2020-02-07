
boogle = [  ['G','I','Z'],
            ['U','E','K'],
            ['Q','S','E']]

def is_valid(x, y):
    if x < 0 or y < 0 or x > 2 or y > 2:
        return False
    else:
        return True

def is_present(x, y, ch, list):

    if x < 0 or y < 0 or x > 2 or y > 2:
        return x, y, False

    if (x,y) not in list and boogle[x][y] == ch:
        return x, y, True
    else:
        r = (x+1, y) not in list and is_valid(x+1, y) and (boogle[x+1][y] == ch)
        if r:
            return x+1, y, True
        else:
            r = (x-1, y) not in list and is_valid(x-1, y) and (boogle[x-1][y] == ch)
            if r:
                return x-1, y, True
            else:
                r = (x, y+1) not in list and is_valid(x, y+1) and (boogle[x][y+1] == ch)
                if r:
                    return x, y+1, True
                else:
                    r = (x, y-1) not in list and is_valid(x, y-1) and (boogle[x][y-1] == ch)
                    if r:
                        return x, y-1, True
                    else:
                        r = (x-1, y-1) not in list and is_valid(x-1, y-1) and (boogle[x-1][y-1] == ch)
                        if r:
                            return x-1, y-1, True
                        else:
                            r = (x-1, y+1) not in list and  is_valid(x-1, y+1) and (boogle[x-1][y+1] == ch)
                            if r:
                                return x-1, y+1, True
                            else:
                                r = (x+1, y-1) not in list and is_valid(x+1, y-1) and (boogle[x+1][y-1] == ch)
                                if r:
                                    return x+1, y-1, True
                                else:
                                    r = (x+1, y+1) not in list and is_valid(x+1, y+1) and (boogle[x+1][y+1] == ch)
                                    if r:
                                        return x+1, y+1, True
                                    else:
                                        return None, None, False

    return x, y, r

x = 0
y = 0
words = ['GEEKS', 'QUIZ', 'FOR']
list = []
for w in words:
    for s in w:
        x, y, res = is_present(x, y, s, list)
        print('got ', x, y, ' for ', s)
        if res:
            list.append((x,y))
        if not res:
            print('not present')
            break
