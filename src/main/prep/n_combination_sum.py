
n = 5

def recursive(n, i):

    if n <1 or i>n:
        return

    print(i, n-i)
    recursive(n-i, i+1)
    recursive(n, i+1)

def iter():

    for x in range(1, n):

        print(x, n-x)
        r = n-x
        l = []
        l.append(x)

        while r > 1:
            l.append(1)
            tmp = []
            tmp.extend(l)
            tmp.append(r-1)
            print( tmp)
            r = r-1

recursive(5, 1)

