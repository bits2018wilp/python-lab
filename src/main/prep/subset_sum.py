
arr = [2, 3, 5, 6, 8, 10]
k = 10
print(arr)

def find_subset(arr, k, lst, bool, goal):

    #print(lst)

    if k == 0 or len(arr) == 0 or sum(lst) == goal:
        print(lst)
        return

    for i in range(len(arr)):

        tmp = arr.copy()
        kc = k

        if bool:
            lst = []

        t = tmp[i]
        tmp.remove(t)

        if t <= kc :
            if sum(lst) + t <= goal:
                kc = kc - t
                lst.append(t)
                find_subset(tmp, kc, lst, False, goal)

lst = []
find_subset(arr, k, lst, True, 10)
