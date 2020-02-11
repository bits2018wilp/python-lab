
num1 = [0, 1, 0, 1]
num2 = [0, 1, 1, 0]

op = []

i = len(num1)-1
bal = 0

while i >=0:

    if num1[i] == 0 and num2[i] == 0 and bal == 0:
        op.append(0)
    elif num1[i] == 0 and num2[i] == 0 and bal == 1:
        op.append(1)
        bal = 0
    elif num1[i] == 0 and num2[i] == 1 and bal == 0:
        op.append(1)
    elif  num1[i] == 0 and num2[i] == 1 and bal == 1:
        op.append(0)
        bal = 1
    elif num1[i] == 1 and num2[i] == 0 and bal == 0:
        op.append(1)
    elif num1[i] == 1 and num2[i] == 0 and bal == 1:
        op.append(0)
        bal = 1
    elif num1[i] == 1 and num2[i] == 1 and bal == 0:
        op.append(0)
        bal = 1
    elif num1[i] == 1 and num2[i] == 1 and bal == 1:
        op.append(1)
        bal = 1
    i-=1
    print(op)

print(bal, op[::-1])


