
def max_number(s, k, lst):

    if k == 0:
        return

    for j in range(0, len(s)):
        for i in range(j, len(s)):

            if s[i] > s[j]:
                tmp = list(s)
                t = tmp[j]
                tmp[j] = tmp[i]
                tmp[i] = t
                tmp = ''.join(tmp)

                if int(tmp) > max(lst):
                    t = lst[0]
                    lst.remove(t)
                    lst.append(int(tmp))
                max_number(tmp, k - 1, lst)

s = '3435335'
lst = []
lst.append(-99999)
k = 3
max_number(s, k, lst)
print(lst)