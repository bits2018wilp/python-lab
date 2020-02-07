
def word_break(word, arr, lst):

    if len(arr) == 0:
        return

    for i in range(len(arr)):

        tlst = None
        if lst is None:
            tlst = []
        else:
            tlst = lst.copy()

        v = arr[i]
        tarr = arr.copy()
        tarr.remove(v)
        if v == word or ''.join(tlst) == word:
            print(tlst)
            break
        elif v in word:
            tlst.append(v)
            word_break(word, tarr, tlst)

word = 'mobileilikemango'
arr= [ 'i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice', 'cream', 'icecream', 'man', 'go', 'mango']
word_break(word, arr, None)