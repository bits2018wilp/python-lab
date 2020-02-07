import math

def is_prime_number(n, prime_numbers):

    if n in prime_numbers:
        return True

    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False

    prime_numbers.append(n)
    #print(prime_numbers)
    return True


def is_ugly(n, prime_numbers, ugly_numbers):

    l = []

    if n%2 == 0:
        l.append(2)
    print('pm = ', prime_numbers)
    print('un = ', ugly_numbers)

    start = 3
    # if len(prime_numbers)> 0:
    #      start = max(prime_numbers)
    # print('n = ', n, ' start = ', start)

    for i in range(start, n+1):
        if  (is_prime_number(i, prime_numbers) and n%i == 0) :
            l.append(i)
        # else:
        #     print(i)

    #print(l)
    if 2 in l:
        l.remove(2)
    if 3 in l:
        l.remove(3)
    if 5 in l:
        l.remove(5)

    if len(l) > 0:
        #print('not ugly')
        return False
    else:
        #print('ugly number')
        ugly_numbers.append(n)
        return True

def dp_ugly_number(n):

    ugly = [None] * n

    ugly[0] = 1
    i2 =0
    i3 =0
    i5 =0

    nm2 = ugly[i2] * 2
    nm3 = ugly[i3] * 3
    nm5 = ugly[i5] * 5


    for i in range(1, 150):

        nun = min(nm2, nm3, nm5)
        ugly[i] = nun

        if nun == nm2:
            i2 +=1
            nm2 = ugly[i2]*2

        if nun == nm3:
            i3 +=1
            nm3 = ugly[i3]*3

        if nun == nm5:
            i5 +=1
            nm5 = ugly[i5]*5


    print(nun)

if __name__ == "__main__":

    dp_ugly_number(150)

    # n =150
    # c = 1
    # i = 2
    # prime_numbers = []
    # ugly_numbers = []
    # while c < n:
    #     b = is_ugly(i, prime_numbers, ugly_numbers)
    #     if b:
    #         print(i, c)
    #         c+=1
    #     i+=1