import math

a = 4
b = 1
c = 2

f2 = math.factorial(b) / (math.factorial(0) * math.factorial(b - 0))
f3 = math.factorial(c) / (math.factorial(0) * math.factorial(c - 0))
f1 = math.factorial(a) / (math.factorial(0 + 0) * math.factorial(a - 0+0))
a1 = f1 * f2 * f3
print(a1)

f2 = math.factorial(b) / (math.factorial(1) * math.factorial(b - 1))
f3 = math.factorial(c) / (math.factorial(0) * math.factorial(c - 0))
f1 = math.factorial(a) / (math.factorial(1 +0) * math.factorial( a - (1+0)))
a1 = f1 * f2 * f3
print(a1)

f2 = math.factorial(b) / (math.factorial(1) * math.factorial(b - 1))
f3 = math.factorial(c) / (math.factorial(1) * math.factorial(c - 1))
f1 = math.factorial(a) / (math.factorial((1 +1)) * math.factorial(a - (1+1)))
a1 = f1 * f2 * f3
print(a1)

f2 = math.factorial(b) / (math.factorial(0) * math.factorial(b - 0))
f3 = math.factorial(c) / (math.factorial(1) * math.factorial(c - 1))
f1 = math.factorial(a) / (math.factorial(0 +1) * math.factorial(a - (0+1)))
a1 = f1 * f2 * f3
print(a1)

f2 = math.factorial(b) / (math.factorial(0) * math.factorial(b - 0))
f3 = math.factorial(c) / (math.factorial(2) * math.factorial(c - 2))
f1 = math.factorial(a) / (math.factorial(0 +2) * math.factorial(a - (0+2)))
a1 = f1 * f2 * f3
print(a1)

f2 = math.factorial(b) / (math.factorial(1) * math.factorial(b - 1))
f3 = math.factorial(c) / (math.factorial(2) * math.factorial(c - 2))
f1 = math.factorial(a) / (math.factorial(1 +2) * math.factorial(a - (1+2)))
a1 = f1 * f2 * f3
print(a1)