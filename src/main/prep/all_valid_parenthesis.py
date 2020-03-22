
def all_valid_parenthesis(n, m, lst):
    print(''.join(lst))

    if n == 0 or m == 0:
        return

    tmp = []
    if len(lst) > 0:
        tmp = lst.copy()

    tmp.append('(')
    all_valid_parenthesis(n - 1, m, tmp)

    tmp.append(')')
    all_valid_parenthesis(n, m - 1, tmp)


all_valid_parenthesis(2, 2, [])