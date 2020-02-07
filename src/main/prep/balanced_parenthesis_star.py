
s = '(*)'
s = '(()****'
s = ')*('
#s = '(()*())*'
stack = []

for c in s:
    #print(c, stack)

    if c == '(':
        stack.append('(')

    elif c == ')':
        if len(stack) > 0:
            if stack[len(stack)-1] == '(':
                stack.pop()
            elif stack[len(stack)-1] == '*':
                if len(stack) > 1 and stack[len(stack)-2] == '(':
                    stack.pop()
                    stack.pop()
                else:
                    stack.pop()
            elif stack[len(stack)-1] == ')':
                stack.append(c)
        else:
            stack.append(c)
    else:
         stack.append(c)

print(stack)
prev = None
while len(stack) > 0:
    p = stack[0]
    stack.remove(p)
    print(p)

    if prev is None:
        prev = p
    else:
        if prev == '*' and p == ')':
            prev =None
        if prev == '(' and p == '*':
            prev =None
        if prev == '*' and p == '*':
            prev = None

print(stack, prev)

