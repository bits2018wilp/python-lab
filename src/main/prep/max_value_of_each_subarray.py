
from collections import deque

def printMax(arr, n, k):

    Qi = deque()

    for i in range(k):

        while Qi and arr[i] >= arr[Qi[-1]]:
            Qi.pop()

        Qi.append(i)

    print(Qi)
    for i in range(k, n):

        print(str(arr[Qi[0]]) + " ", end="")
        while Qi and Qi[0] <= i - k:
            Qi.popleft()

        while Qi and arr[i] >= arr[Qi[-1]]:
            Qi.pop()

        Qi.append(i)

    print(str(arr[Qi[0]]))


# Driver programm to test above fumctions
if __name__ == "__main__":
    arr = [12, 1, 78, 90, 57, 89, 56]
    arr = [10, 3, 1, 7, 8, 7]
    k = 3
    printMax(arr, len(arr), k)

# This code is contributed by Shiv Shankar
