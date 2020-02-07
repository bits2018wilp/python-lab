
def separator_count(p):

    cnt = 1
    for c in p:
        if c == '|':
            cnt+=1
    return cnt


word = []
seprator  = ['\n', '\t']
root  = ''
subdir = ''
abspath = []
bool = True
i = -1
prev = ''
tabCount = 0
paths = []
path = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext\n\tsubdir3"
print(path)
prevtabcount = 0
prevword = ''
fpaths = []
while i < len(path):

    i+=1
    if i < len(path):
        c = path[i]
    else:
        c = '\n'

    if c not in seprator:
        word.append(c)
    else:
        if c == seprator[0]:
            if root == '':
                root = ''.join(word)
                paths.append(root)
                prev = root
            else:
                tmppaths = []
                if tabCount == 1:
                    for p in paths:
                        if separator_count(p) == 1:
                            tmppaths.append(p)
                    fpaths.append(paths)
                    paths = []
                    paths.extend(tmppaths)
                print(tabCount, ''.join(word), prevword, paths)
                tmppaths = paths.copy()
                for p in tmppaths:
                    if separator_count(p) == tabCount:
                        if '.ext' in p:
                            t = p + '|' + ''.join(word)
                            paths.append(t)
                        else:
                            t = p + '|' + ''.join(word)
                            paths.append(t)
            word = []
            tabCount = 0
        else:
            tabCount+=1

fpaths.append(paths)
print(fpaths)