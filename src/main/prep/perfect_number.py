
pn = 19

n = 15

unit = pn%10
rest = pn//10

print(rest, unit)
c = 1
while True:

    if pn%9 == 1:
        c+=1

    if c == n:
        print(pn)
        break
    else:
        pn+=1

print( str(rest), str(unit) )