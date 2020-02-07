
string = 'this is a test string'
pattern = 'tist'

string = 'geeksforgeeks'
pattern ='ork'
pc = pattern
start = None
stop = None
bool = True
i=0
n = len(string)

while i<n and bool:

    if string[i] in pc:

        pc = list(pc)
        pc.remove(string[i])
        pc = ''.join(pc)

        if start is None:
           start = i

        if len(pc) == 0:
            print(string[start:i+1])
            pc = pattern
            stop = i

    i+=1

window = string[start:stop+1]
print(window)


bool = True
i=0

window = list(window)
pc = pattern
found = False

while not found and bool :

    t = window[0]
    window.remove(t)

    for c in window:
        pc = list(pc)
        if c in pc:
            pc.remove(c)
        pc = ''.join(pc)

    if len(pc) == 0:

        print(''.join(window))
        pc = pattern
    else:
        window.insert(0, t)
        found = True

print(''.join(window))