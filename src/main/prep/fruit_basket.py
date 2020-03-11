
arr = [3,3,3,1,2,1,1,2,3,3,4]
arr = [1,2,3,2,2]

type1 = None
type2 = None
prev = None
c1 = 0
c2 = 0

for i in range(len(arr)):

    if type1 is None or arr[i] == type1:
        type1 = arr[i]
        c1+=1
        prev = type1

    elif type2 is None or arr[i] == type2:
        type2 = arr[i]
        c2+=1
        prev = type2

    else:
        if arr[i] == type1:
            c1+=1
        elif arr[i] == type2:
            c2+=1
        else:
            print('found ', i, arr[i])
            print('count: ' , c1+c2)

            if arr[i-1] == type1:
                type2 = arr[i]
                c2=1
            else:
                type1 = arr[i]
                c1=1

print('count ', c1+c2)