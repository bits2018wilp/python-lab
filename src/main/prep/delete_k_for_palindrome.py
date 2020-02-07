from src.main.prep.counter import Boolean
import time

s = 'waterrfetawx'
s = 'waterretawfx'
s = 'watferretawx'
s = 'watferretawxz'
k = 3
print(len(s)/2)

def find_palindrome(s, k):

    print(s, k)
    if len(s) == 0:
        return True

    i = 0
    j = len(s)-1

    while i <= j :

        time.sleep(2)

        if s[i] == s[j]:
            print('match: ', i , j)
            i+=1
            j-=1
        else:
            break
    print(i, j)
    if i < j:
        if k <= 0:
            return False
        else:
            print(s[i:j])
            b = find_palindrome(s[i:j], k - 1)
            if not b:
                print(s[i+1:j])
                b = find_palindrome(s[i+1:j+1], k - 1)
                return b
            else:
                return True
    else:
        print('palindrome exist..')
        return True

indices = []
bool = Boolean()
bool.set_value(False)
val = find_palindrome(s, k)
print(val)

