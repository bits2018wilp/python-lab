
arr = [3, 4, 7, 2, 5]

dict = {}

i =0
loop = True

while loop:
    f = arr[i]

    for x in range(i+1, len(arr)):

        if x+1 == len(arr)+1:
            break

        sum = arr[x] + f

        if sum in dict:

            t = dict[sum]
            print(t, (f, arr[x]))

        else:

            dict[sum] = (f, arr[x])
    print(dict)
    i+=1
    if i == len(arr):
        loop = False


