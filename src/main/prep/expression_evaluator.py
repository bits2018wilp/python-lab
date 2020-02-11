
exp = "2 + 3 * 6 - 2"
#exp = exp[::-1]
print(exp)

stack = []
tmp = []
postfix = []

op1 = ['*', '/']
op2 = ['+', '-']

for c in exp:

    if c == ' ':
        continue
    c = c.strip(" ")
    print('c:', c)

    if c not in op1 and c not in op2:
        postfix.append(c)
    else:
        if len(stack) == 0:
            stack.append(c)
        else:
            p = stack.pop()
            if c in op1 and p in op2:
                postfix.append(p)
                stack.append(c)
            else:
                
                while True:
                    p = stack.pop()
                    if (p in op1 and c in op2) or (p in op1 and c in op1):
                        postfix.append(p)
                    else:
                        stack.append(c)
                        break

    print('postfix: ', postfix)
    print('stack: ',stack)

while len(stack) > 0:
    p = stack.pop()
    postfix.append(p)

print(postfix)
print(stack)


