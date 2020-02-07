
def reverse(lst, i, j):

    while i < j:
        t = lst[i]
        lst[i] = lst[j]
        lst[j] = t
        i+=1
        j-=1

bool = False
def rev_sort(arr) :

    i = 0
    while True:

        print(arr)
        j = i
        while  i < len(arr)-1 and arr[i] > arr[i+1]:
            i+=1
        reverse(arr, j, i)

        if i == len(arr)-1:
            break
        i+=1

arr= [5,1,3,2,4]
arr = [1,2,3,4,5]
arr = [5,4,3,2,1]
arr = [2,1,3,5,4]
rev_sort(arr)
print(arr)