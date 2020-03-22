
board = [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]
        ]

w = "ABCCED"
w = "ABFSABE"
w = "ABFSABCE"
maxr = 3
maxc = 4
i=0
j=0
tgt = ""
print(tgt)
k = 0
visited = []

def find_word(board, tgt, i, j, k, w):

    if i >=0 and i <maxr and j>=0 and j<maxc:

        #print(i, j, k, tgt)

        if board[i][j] == w[k]:
            tgt = tgt+w[k]
        else:
            return

        if tgt == w:
            print('found')
            return

        find_word(board, tgt, i, j+1, k+1, w)
        find_word(board, tgt, i+1, j, k + 1, w)
        find_word(board, tgt, i-1, j, k + 1, w)
        find_word(board, tgt, i, j - 1, k + 1, w)
    else:
        return

find_word(board, tgt, i, j, k, w)