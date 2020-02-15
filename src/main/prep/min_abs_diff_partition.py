
def min_abs_diff(arr, set1, set2, n):

        for i in range(len(arr)):

            tarr = arr.copy()

            tset1 =  None
            if set1 is None:
                tset1 = []
            else:
                tset1 = set1.copy()

            tset2 =  None
            if set2 is None:
                tset2 = []
            else:
                tset2 = set2.copy()

            if tarr[i] not in tset1:
                tset1.append(tarr[i])

            for s in tset1:
                if s in tarr:
                    tarr.remove(s)

            if len(tarr) == 0:
                continue

            print(tset1, tarr, abs(sum(tarr) - sum(tset1)))
            min_abs_diff(tarr, tset1, tset2, n)


arr = [1, 6, 5, 11, 7]
min_abs_diff(arr, None, None, len(arr))