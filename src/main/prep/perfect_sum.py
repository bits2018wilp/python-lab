from src.main.prep.counter import Counter

def subset_sum(sum, arr, counter, lst):

    if sum == 0:
        print(lst)
        counter.increment()
        return
    else:
        for i in range(len(arr)):
            tlst = None
            if lst is None:
                tlst = []
            else:
                tlst = lst.copy()
            tsum = sum
            v = arr[i]
            if v == tsum:
                tlst.append(v)
                subset_sum(0, [], counter, tlst)
            elif tsum - v >= 0:
                tsum = tsum - v
                tlst.append(v)
                tarr = arr.copy()
                tarr.remove(v)
                subset_sum(tsum, tarr, counter, tlst)

sum = 11
arr= [2,3,5,6,8,10]
cnt = Counter(0)
subset_sum(sum, arr, cnt, None)
print(cnt)