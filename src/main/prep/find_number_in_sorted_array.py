
arr = [1, 3, 4, 5, 7, 10, 14, 15, 16, 19, 20, 25]
k = 16

def elementAt(arr, j):

    if j > len(arr)-1 or j < 0:
        return -1
    else:
        return arr[j]

i = 0
while True:

   t = elementAt(arr, i)
   if t == k:
       print(i)
       break
   elif t > k:
       i-=2
   elif t <k:
       i+=2
   elif t == -1:
       if i < 0:
           i+=2
       else:
           i-=2
