
input = '()()(((()))(((((())'
input = '()())()'
input = ')('

stack = []
arr = []
for i in input:

    if i == '(':
        stack.append(i)
    elif i == ')':
        if len(stack) == 0:
            arr.append(i)
        else:
            j = stack.pop()
            if j != '(':
                raise Exception ("un balanced quote")

if len(stack) > 0 or len(arr)> 0:
    raise Exception("un balanced quote stack", stack, arr)
