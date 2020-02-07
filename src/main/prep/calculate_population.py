
lst  =  [(1900, 1945), (1940, 1960), (1950, 1980),  (1955, 1990), (1980, 2000)]

born = [1950, 1940, 1955, 1980, 1900]

died = [1980, 1960, 1990, 2000, 1945]

all = born + died
all.sort()

born.sort()
died.sort()

c = 0
m = 0

for d in all:

    if d in born:
        c+=1

    if d in died:
        c-=1

    if c > m:
        m = c

print(m)