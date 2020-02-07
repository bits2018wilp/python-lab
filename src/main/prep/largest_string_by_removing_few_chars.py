
words = ["ale", "apple", "monkey", "plea"]
words = ["pintu", "geeksfor", "geeksgeeks", " forgeek"]

s = 'abpcplea'
s= 'geeksforgeeks'

words.sort(key = lambda x : len(x), reverse=True)
print(words)

result = []

for w in words:

    result.append(w)
    for i in w:
        if i not in s:
            result.remove(w)
            break

print(result)
