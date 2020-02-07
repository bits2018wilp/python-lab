
x = 20
x = 105

for i in range(x):

    if i < 10:
        print(i)
    else:
        s = str(i)
        b = True

        for j in range(0, len(s)-1):

            if abs(int(s[j]) - int(s[j+1])) != 1:
                b = False
                break
        if b:
            print(i)