
arr = [2, 7, 6, 9, 10, 2, 6, 10]
#arr = [2, 6, 10, 2, 6, 10]

#  0111
#  1001
#  1110

ans = None

for x in arr:

    if ans == None:
        ans = x
    else:
        ans = ans^x

print(ans)

x1 = bin(ans)
print(x1)

# make a number which has only 1 set bt of xor result

x1 = str(x1)
x1 = x1[2:]
x2 = []
notset = True
for i in x1:
    if i == '1' and notset:
        x2.append('1')
        notset = False
    else:
        x2.append('0')

print(x2)
print(int(''.join(x2)))
x3 = bin(8)

p =0
q= 0

for z in arr:
    print(z&8)
    if z & 8 == 0:
        p = p ^ z
    else:
        q = q ^ z
print(p, q)