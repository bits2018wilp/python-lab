import math

a = 81
a = 271
lst = []
i = 2

while a>1:
    if a%i == 0:
        lst.append(i)
        a = a//i
    else:
        i+=1

print(a, i, lst)