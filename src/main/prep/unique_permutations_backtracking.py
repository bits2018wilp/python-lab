
def shouldSwap(string, start, curr):

    for i in range(start, curr):
        if string[i] == string[curr]:
            return 0
    return 1


def findPermutations(string, index, n):

    if index >= n:
        print(''.join(string))
        return

    for i in range(index, n):

        check = shouldSwap(string, index, i)
        #print('check: ', index, i, check)
        if check:
            print('swaping ', index, i)
            string[index], string[i] = string[i], string[index]
            findPermutations(string, index + 1, n)
            string[index], string[i] = string[i], string[index]

def findAll(string, lst):

    if len(string) == 0:
        print(''.join(lst))
        return

    dupe = []
    for i in range(len(string)):

        if string[i] in dupe:
            continue
        else:
            dupe.append(string[i])

        tmp= []
        if lst:
            tmp = lst.copy()

        tmp.append(string[i])
        findAll(string[:i]+string[i+1:], tmp)


if __name__ == "__main__":
    string = list("ABCA")
    #findPermutations(string, 0, len(string))
    findAll(string, [])