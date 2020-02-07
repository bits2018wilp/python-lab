

def maxProfit(price, n, k):
    # Table to store results of subproblems
    # profit[t][i] stores maximum profit
    # using atmost t transactions up to
    # day i (including day i)
    profit = [
              [0 for i in range(n + 1)]
              for j in range(k + 1)]
    print(profit)

    # Fill the table in bottom-up fashion
    for i in range(1, k + 1):

        prevDiff = float('-inf')

        for j in range(1, n):

            prevDiff = max(prevDiff,
                           profit[i - 1][j - 1] -  price[j - 1])

            profit[i][j] = max(profit[i][j - 1],   price[j] + prevDiff)

    return profit[k][n - 1]


arr = [ 10, 22, 5, 75, 65, 80 ]

profit = maxProfit(arr, 6, 2)
print(profit)
