matrix = [[1, 1, 3],
          [1, 0, 2],
          [0, 1, 0]
]

visited = []
visited.append('00')

target = "22"

bool = True
i = 0
j = 0
import math

def mini(c1, c2):

    v1 = (c1[0] - 2)*(c1[0] - 2) + (c1[1] - 2)*(c1[1] - 2)
    v1 = math.sqrt(v1)

    v2 = (c2[0] - 2) * (c2[0] - 2) + (c2[1] - 2) * (c2[1] - 2)
    v2 = math.sqrt(v2)

    if matrix[c1[0]][c1[1]] > matrix[c2[0]][c2[1]]:
        return c2
    elif matrix[c1[0]][c1[1]] < matrix[c2[0]][c2[1]]:
        return c1
    else:
        if v1 > v2:
            return c1
        else:
            return c2


while bool:

        is_target = None
        tt = None

        if j+1 < 3:
            p1 = matrix[i][j+1]
            if str(i)+str(j+1) == target:
                is_target=True
                tt = str(i)+str(j+1)
        else:
            p1 = 9999

        if i+1 < 3:
            p2 = matrix[i+1][j]
            if str(i+1)+str(j) == target:
                is_target=True
                tt = str(i+1) + str(j)
        else:
            p2 = 9999

        if i+1 < 3 and j+1< 3:
            p3 = matrix[i+1][j+1]
            if str(i+1)+str(j+1) == target:
                is_target=True
                tt = str(i+1) + str(j + 1)
        else:
            p3 = 9999

        if is_target:
            visited.append(tt)
            bool = False
            continue

        minp = min(p3, min(p1, p2))

        if minp == p3:
            visited.append(str(i+1)+str(j+1))
            j+=1
            i+=1
        elif minp == p2:
            visited.append(str(i+1) + str(j))
            i+=1
        else:
            visited.append(str(i) + str(j + 1))
            j+=1

        current = str(i)+ str(j)
        if target == current:
            bool = False

print(visited)
