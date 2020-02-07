from src.main.prep.counter import Object

arr = [23, 13, 25, 29, 33, 19, 34, 45, 65, 67]
arr = [23, 13, 25, 29, 33, 19, 34, 45, 65, 64]
arr = [100, 180, 260, 310, 40, 535, 695]

#arr = [9, 11, 8, 5, 7, 10]
arr = [5, 2, 4, 0, 1, 7, 6, 9]

def k_buy_sell(arr, k, buy, profit):

    if len(arr) == 0 or k == 0:
        if k == 0:
            print(profit)
        return

    for i in range(len(arr)):
        if buy is None or buy.get() == -99:
            buyt = Object()
            buyt.set(arr[i])
            k_buy_sell(arr[i+1:], k, buyt, profit.copy())
        else:
            if arr[i] > buy.get():
                p = profit.copy()
                p.append((buy.get(), arr[i]))
                k_buy_sell(arr[i+1:], k-1, None, p)

k_buy_sell(arr, 3, None, [])


def trade1 (arr):
    buy = None
    sell = None
    series = []
    i = 1

    while i < len(arr):
        print(i, buy, sell)

        if buy is None:
            if arr[i] < arr[i-1]:
                buy = arr[i]
            else:
                buy = arr[i-1]

        else:
            if i == len(arr)-1:
                if arr[i] > arr[i-1] and arr[i] > buy:
                    sell = i
                else:
                    if arr[i-1] > buy:
                        sell = i-1
            elif arr[i] > arr[i+1] and arr[i] > buy:
                sell = i


        if buy is not None and sell is not None:
            series.append((buy, sell))
            buy = None
            sell = None
            i+=2
        else:
            i+=1

def only_one_txn(arr):

    i = 0
    buy = 9999999
    sell = 0
    bi =0
    si =0

    while i < len(arr):

        if arr[i] < buy:
            buy = arr[i]
            bi =i

        if arr[i] > buy:
            sell = arr[i]
            si =i

        i+=1
        if sell > buy and si > bi:
            print(buy, sell)

#only_one_txn(arr)