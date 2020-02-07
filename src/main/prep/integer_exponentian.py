
def epow(x, y):

    t = 2
    ans = x * x

    while y-(t*2) > 0:

        print(ans, t)
        ans = ans * ans
        t = t * 2

    print(ans, t)
    return ans, t

y = 12
ans, t = epow(2, y)

y = y - t

if y < 1:
    y = -1 * y
    while y > 0:
        ans = ans/2
        y = y-1
elif y > 1:
    while y > 0:
        ans = ans*2
        y = y-1
print(ans)