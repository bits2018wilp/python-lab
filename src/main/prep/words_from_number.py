
arr = [1, 2, 2, 1]

# 1,2,2,1  12, 2, 1   12, 21   1, 22, 1    1, 2, 21

list = []
list.append(arr)
print(list)
loop = True
i=0
j=0

def break_arr(arr, list):

    if len(arr) == 0:
        return

    x = ''.join([ str(s) for s in arr[0:2]])

    if int(x) <= 26 :
        t = (x, arr[2:])
        list.append(t)
        break_arr(arr[2:], list)
    else :
        t = (arr[0:1], arr[1:])
        list.append(t)
        break_arr(arr[1:], list)

list = []
break_arr(arr, list)
print(list)



