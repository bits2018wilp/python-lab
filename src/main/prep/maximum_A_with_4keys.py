
n = 4 # AAAA
n = 5 # AAAAA
n = 6 # AAAAAA

n = 7 # AAA  AC AAA AAA   pppscvv
n = 8 # AAA AC AAA AAA AAA   pppscvvv
n = 9 # AAAA AC V AAAA CAV AAAA


def selectCopyPaste(list1, c, clipboard):


    if len(list1) <= 2:
        return c, list1

    print('selectcopypaste')

    tmplist = list1.copy()
    if c - 3 >= 0:
        c = c-3

        clipboard.clear()
        for x in list1:
            clipboard.append(x)

        for x in clipboard:
            tmplist.append(x)

    return c, tmplist


def paste(list1, c, clipboard):

    if len(clipboard) ==0:
        return c, list1

    print('paste')
    tmplist = list1.copy()
    if c  > 0:
        c = c - 1
        for x in clipboard:
            tmplist.append(x)

    return c, tmplist


def typeA(list1, c):
    tmp =  list1.copy()
    print('typeA')
    if c  > 0:
        c = c - 1
        tmp.append('A')

    return c, tmp

def countA(c, llist):

    if c == 0:
        return

    ac, typAlist = typeA(llist, c)
    oldclipboard = clipboard.copy()
    bc, scpList = selectCopyPaste(llist, c, clipboard)
    cc, plist =  paste(llist, c, oldclipboard)

    if len(typAlist) >= len(scpList) and len(typAlist) >= len(plist):
        llist = typAlist.copy()
        c = ac
    elif len(scpList) >= len(typAlist) and len(scpList) >= len(plist):
        llist = scpList.copy()
        c = bc
    elif len(plist) >= len(scpList) and len(plist) >= len(typAlist):
        llist = plist.copy()
        c = cc

    print(llist, len(llist), c)
    countA( c, llist )

llist = []
clipboard = []
llist.append('A')
countA(8, llist)