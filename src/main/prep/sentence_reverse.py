
sentence = 'the sky is blue '
sentence = "  hello world!  "
arr = sentence.split(' ')
for x in arr.copy():
    if x == '':
        print('space')
        arr.remove('')
print(arr)
arr.reverse()
print(' '.join(arr))