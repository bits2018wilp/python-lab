

def is_palindrome(arr):
    i = 0
    j = len(arr)-1
    while i < j:
        if arr[i] != arr[j]:
            return False
        else:
            i+=1
            j-=1
    return True

s = 'aabcdcb'
s = 'bananas'
i = 0
j = 1
results = []

def find_palindromes(s):
    global results

    if len(s) <2:
        return

    if is_palindrome(s):
        results.append(s)
    else:
        s2 = s[0:len(s)-1]
        s1 = s[1:len(s)]

        find_palindromes(s1)
        find_palindromes(s2)

find_palindromes(s)
print(results)