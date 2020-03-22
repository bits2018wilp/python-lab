
def generate(k):

    pascal= []

    for i in range(k):

        arr = []
        prevarr = None
        if i > 0:
            prevarr = pascal[i-1]
            print(prevarr)
        for j in range(i+1):
            print('j: ', j)
            if i == 0:
                arr.append(1)
            else:
                if j - 1 < 0:
                    arr.append(prevarr[j])
                elif j >= len(prevarr):
                    arr.append(prevarr[j-1])
                else:
                    arr.append(prevarr[j] + prevarr[j-1])

        pascal.append(arr)

    return pascal

pascal = generate(6)
print(pascal)
