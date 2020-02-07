
arr = [ (2, 6), (3, 4), (0, 3), (6, 9) ]
# 0 2 3 4 6 9
arr = [  (10, 20), (10, -20) ]

#get largest min and  smallest max
#  shrink from right to left nand left to right.  find smallest from end side and largest from start side

smallest = 99999
largest = -99999

for t in arr:

    s = t[0]
    e = t[1]

    if e < smallest:
        smallest = e

    if s > largest:
        largest = s


print(smallest, largest)