
arr = [1, 3, 2]
# arr = [1, 2, 3]
arr = [3, 1, 2]
arr = [3, 1, 2, 8, 7]

#arr = [2, 1, 3]
#arr = [2, 3, 1]
#arr = [3, 2, 1]

def find_next_big(arr):

    i = len(arr)-1
    bool = True
    j = None

    while i>0:

        if arr[i-1] < arr[i]:
            j = i-1
            bool= False
        i-=1

    print(i, j)
    t = j+1

    if bool:
        print('not possible')

    smallest = arr[j+1]
    si = j+1
    print(i, j, t, smallest)

    while t < len(arr):
        if arr[t] > smallest and arr[t] < arr[si]:
            si = t
        t+=1

    print(si)
    tmp = arr[j]
    arr[j] = arr[si]
    arr[si] = tmp
    arr = arr[0:si] + sorted(arr[si:])

    return arr


def findNext(number, n):
    # Start from the right most digit and find the first
    # digit that is smaller than the digit next to it

    for i in range(n - 1, 0, -1):
        if number[i-1] < number[i]:
            break

    # If no such digit found,then all numbers are in
    # descending order, no greater number is possible

    if i == 0:
        print("Next number not possible")
        return

    # Find the smallest digit on the right side of
    # (i-1)'th digit that is greater than number[i-1]
    x = number[i - 1]
    smallest = i
    print(x, i)

    for j in range(i + 1, n):
        if number[j] > x and number[j] < number[smallest]:
            smallest = j

    number[smallest], number[i - 1] = number[i - 1], number[smallest]
    number = number[:i] + sorted(number[i:])
    return number

print(arr)
#arr1 = find_next_big(arr)
arr2 = findNext(arr, len(arr))
print( arr2)
