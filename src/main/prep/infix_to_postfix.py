
expr = 'a+b*c-d/e'
#  a+g-h
#  abc*de/-+
#  abc*+de/-

op = ['+', '-', '/', '*']

opstack = []

stack = []
hold = []

for e in expr:

    if e not in op:
        stack.append(e)
    else:
        if len(opstack) == 0:
            opstack.append(e)
        else:
            if e in ['+', '-'] and opstack[len(opstack)-1] in ['*', '/']:
                 while len(opstack) > 0:
                     t = opstack.pop()
                     stack.append(t)
                 opstack.append(e)
            else:
                opstack.append(e)

while len(opstack) > 0:
    t = opstack.pop()
    stack.append(t)

print(stack)

