

x = 12
N = 6

multiples = []
for i in range(1, x//2+1):

    if x%i == 0 and i <= N:
        multiples.append(i)

print(multiples)

for i in range(len(multiples)):

    for j in range(i+1, len(multiples)):

        if multiples[i] *  multiples[j] == x:
            print(multiples[i]-1, multiples[j]-1)
            print(multiples[j] - 1, multiples[i] - 1)
