
def push(stack, val):

    tmp = []
    if len(stack) == 0:
        stack.append(val)
    else:
        while len(stack)>0 and val > stack[len(stack)-1]:
            p = stack.pop()
            tmp.append(p)

        stack.append(val)
        while len(tmp) > 0:
            p = tmp.pop()
            stack.append(p)
    print(stack)
stack = []
push(stack, 3)
push(stack, 1)
push(stack, 5)
push(stack, 2)
print(stack)
print(stack.pop(), stack.pop(), stack.pop(), stack.pop())