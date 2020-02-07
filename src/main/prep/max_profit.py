from src.main.prep.counter import Counter

def maxPRecursive(prices, k, buy, profit_list):

    if k == 0:
        return

    fm = 0
    for i in range(len(prices)):
        prices2 = prices[i+1:]
        for j in range(len(prices2)):
                maxp = prices2[j]-prices[i]
                prices3 = prices2[j+1:]
                for i2 in range(len(prices3)):
                    prices4 = prices3[i2+1:]
                    for j2 in range(len(prices4)):
                            maxp2 = prices4[j2] - prices3[i2]
                            print(i, j, i2, j2, maxp, maxp2)
                            fm = max(fm, maxp+maxp2)

    return fm


def recur(prices, k, counter):

    if k == 0:
        return 0

    fm = 0
    for i in range(len(prices)):
        prices2 = prices[i+1:]
        for j in range(len(prices2)):
            prof = prices2[j] - prices[i]
            fm = max(fm, prof + recur(prices2[j:], k-1, counter.increment()))

    return fm


def maxProfit(prices, n, k):
    # Bottom-up DP approach
    profit = [
                [0 for i in range(k + 1)] for j in range(n)
            ]
    print(profit)
    # Profit is zero for the first
    # day and for zero transactions
    for i in range(1, len(prices)):

        for j in range(1, k + 1):
            max_so_far = 0

            for l in range(i):
                max_so_far = max(max_so_far, prices[i] -  prices[l] + profit[l][j - 1])

            profit[i][j] = max( profit[i - 1][j], max_so_far)

    print(profit)
    return profit[n - 1][k]

# Driver code
k = 2
prices = [10, 22, 5, 3, 75, 65, 80]
n = len(prices)

print("Maximum profit is:",  maxProfit(prices, n, k))

# pl =[]
# p = maxPRecursive(prices, 2, None, pl)
# print(p)
counter = Counter(0)
p = recur(prices, 3, counter)
print(p, counter)