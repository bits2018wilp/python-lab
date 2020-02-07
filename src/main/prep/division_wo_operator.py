
n = 115
d = 24

if d == 0:
    raise ZeroDivisionError

if n < d:
    print('quotient: ', 0)
else:
    count = 0
    while n >= d:
        n = n-d
        count+=1
    print('quotient: ', count)