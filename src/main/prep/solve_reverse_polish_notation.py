
arr= [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']

stack = []

i = 0
bool = True

while i< len(arr):

    e = arr[i]
    if e == '-':
        op1 = stack.pop()
        op2 = stack.pop()
        stack.append(op2-op1)
    elif e == '+':
        op1 = stack.pop()
        op2 = stack.pop()
        stack.append(op2 + op1)
    elif e == '*':
        op1 = stack.pop()
        op2 = stack.pop()
        stack.append(op2 * op1)
    elif e == '/':
        op1 = stack.pop()
        op2 = stack.pop()
        stack.append(op2 / op1)
    else:
        stack.append(e)
    i+=1

print(stack)