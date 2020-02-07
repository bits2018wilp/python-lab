
def is_palindraome(arr):

    if len(arr) <= 1:
        return False

    i = 0
    j = len(arr) - 1

    while i<j:
        if arr[i] != arr[j]:
            return False
        i+=1
        j-=1
    return True


def palindrome(string, substr, c):

    if len(string) == 0:
        return

    if c == 0:
        for i in range(len(string)):

            tmpsubstr = None
            if substr is None:
                tmpsubstr = []
            else:
                tmpsubstr = substr.copy()

            tmpsubstr.append(string[i])
            tmps = string[i+1:]

            if is_palindraome(tmpsubstr):
                print(tmpsubstr)
            palindrome(tmps, tmpsubstr, c+1)
    else:
        s = string[0]
        tmpsubstr = None
        if substr is None:
            tmpsubstr = []
        else:
            tmpsubstr = substr.copy()

        tmpsubstr.append(s)
        tmps = string[1:]

        if is_palindraome(tmpsubstr):
            print(tmpsubstr)
        palindrome(tmps, tmpsubstr, c + 1)

palindrome('abbaeae', None, 0)
