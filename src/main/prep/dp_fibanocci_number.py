
def dp_fib(n, i, fl):

    if n == i:
        return

    fl[i] = fl[i-1] + fl[i-2]
    dp_fib(n, i+1, fl)


fl = [None] * 100
fl[0] = 0
fl[1] = 1

dp_fib(100, 2, fl)
print(fl)