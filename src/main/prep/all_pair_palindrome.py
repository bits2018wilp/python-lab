
lst = ["code", 'd', "da", "edoc", 'ad']

visited = []

def is_palindrome(s1, s2, p, q):
    #print(p, q)
    c1 = 0
    c2  = 0

    s = s1+s2
    i = 0
    j = len(s)-1
    while i<=j:
        if s[i] != s[j]:
            c1 = 1
        i+=1
        j-=1

    s = s2 + s1
    i = 0
    j = len(s) - 1
    while i <= j:
        if s[i] != s[j]:
            c2 = 1
        i+=1
        j-=1

    if c1 == 0 and c2 ==0:
        return [(p,q), (q,p)]
    elif c1 == 1 and c2 ==0:
        return [(q,p)]
    elif c1 == 0 and c2 == 1:
        return [(p, q)]
    else:
        return False
    
i = 0
c= 0
while i < len(lst):
    
    j = i+1
    
    while j < len(lst) and i not in visited :
        c+=1
        #print(visited)
        is_pal = is_palindrome(lst[i], lst[j], i, j)
        if is_pal != False:
            if len(is_pal) == 2:
                print(is_pal)
                visited.append(is_pal[0][0])
                visited.append(is_pal[0][1])
            else:
                print(is_pal)
                #visited.append(is_pal[0][1])
        j+=1
    i+=1

    
print(c)