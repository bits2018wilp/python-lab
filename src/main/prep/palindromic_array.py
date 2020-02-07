
arr = [ 3, 2, 3, 3, 5 ]
arr = [1,3,4,4,4]
lst = []
i = 0
j = len(arr) -1

bool = True
c =0
while  bool:

    if arr[i] == arr[j]:
        lst.append(arr[i])
        lst.append(arr[j])
        i+=1
        j-=1
    else:

        if arr[i] < arr[j]:
            p = i+1
            s = sum(arr[i : p+1])
            if s == arr[j]:
                c+=1
                lst.append(s)
                lst.append(arr[j])
                i = p
                j-=1
            else:
                i+=1
        else:
            p = j-1
            s = sum(arr[p : j+1])
            if s == arr[i]:
                c+=1
                lst.append(s)
                lst.append(arr[i])
                j = p
                i+=1
            else:
                j-=1

    if i == j or i > j:
        bool = False

print(lst, c)