
s = 'geeksforgeeks'
s = 'bbbabaaacd'
stack = []
hold = []

lastchar = None

for c in s:

    if len(stack) == 0:
        stack.append(c)
        lastchar = c
    else:
        if c != lastchar:
            lastchar = c
            stack.append(c)
            if hold and len(hold)>0 and c != hold[0]:
                stack.append(hold[0])
                lastchar = hold[0]
                hold.remove(lastchar)
        else:
            hold.append(c)

print(stack)
print(hold)