
m = 3
n = 3
k = 2

# 00 01 02
# 10 11 12
# 20 21 22

arr = [
      [0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]
     ]

def attack(i, j, arr):

    

def can_place(i, j, arr):

    if arr[i][j] == 0:
        return True
    else:
        return False

def place(i, j, arr):

    tmparr = arr.copy()
    tmparr[i][j] = 1

    attack(i, j, tmparr)

for i in range(m):
    for j in range(n):

