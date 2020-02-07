
arr = [ 5, 2, 1, 4, 6, 7, 9 ]

stack = []

stack.append(arr[0])

for i in range(1, len(arr)):

    if arr[i] > stack[len(stack)-1]:
        bol = True
        while bol :
            if len(stack) > 0 and arr[i] > stack[len(stack)-1]:
                t = stack.pop()
                print('max for ', t, ' is ', arr[i])
            else:
                bol=False
        stack.append(arr[i])
    else:
        stack.append(arr[i])

for x in stack:
    print('max for ', x, ' is ',-1)