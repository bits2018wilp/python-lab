arr = [7, 4, 0, 9, 11, 6, 5, 8]
arr = [0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0]
# arr = [7, 4, 0, 9, 6, 5, 8]
# arr = [3, 0, 0, 2, 0, 4]
#arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
#arr = [7, 4, 0, 5, 6, 5, 4]

# Python program to find maximum amount of water that can
# be trapped within given set of bars.


def findw(arr):

    left = [0] * len(arr)
    left[0] = arr[0]
    for i in range(1, len(arr)):
        left[i] = max(left[i-1], arr[i])

    right = [0] * len(arr)
    right[len(arr)-1] = arr[len(arr)-1]
    for i in range(len(arr)-2, -1, -1):
        right[i] = max(right[i+1], arr[i])

    water = 0
    for i in range(0, len(arr)):
        print(left[i], right[i], arr[i])
        water += min(left[i], right[i]) - arr[i]

    print(arr)
    print(left)
    print(right)
    print(water)


findw(arr)