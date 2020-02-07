
s  = 'figehaeci'

chars = ['a', 'e', 'i']

i = 0
j = len(chars)

prev = None

def has_chars(s, arr):

    for a in arr:
        if a not in s:
            return False
    return True

while j <= len(s):

    if has_chars(s[i:j], chars):
        print(i, j, s[i:j])
        prev = s[i:j]
        i+=1
        while j-i >= len(chars) and has_chars(s[i:j], chars):
            if len(s[i:j]) < len(prev):
                prev = s[i:j]
                print(i, j, prev)
                i+=1
    else:
        j+=1