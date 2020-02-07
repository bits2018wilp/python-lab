
c = 97
map = {}
for i in range(1, 27):
    map[chr(c)] = i
    c+=1
print(map)

revmap = {}
for k,v in map.items():
    revmap[v] = str(k)
print(revmap)

msg = 12123
msg = str(msg)
print(msg)

bool = True

i = 0
r = 1

# while bool:
#     dm = []
#     for i in range(len(msg)):
#         if int(msg[i]) in revmap:
#             dm.append(revmap[int(msg[i])])
#     print(dm)
#     bool = False

# 1213 ==>  1,2,1,3  12,1,3  1, 21, 3   1,2,13  12, 13
# 12123  ==> 1,2,1,2,3  12,1,2,3   1,21,2,3   1,2,12,3   1,2,1,23   12,12,3   1,21,23  12,1,23

bool = True
flst = []
k = 2
i = 0
jumpos = 0
msg = list(msg)
tmplst = []

while bool:

    if i == jumpos:
        tmpmsg = msg[i : i+k]
        i+=k
    else:
        tmpmsg = msg[i : i + 1]
        i+=1

    if len(tmpmsg) > 0 and int(''.join(tmpmsg)) < 27:
        tmplst.append(''.join(tmpmsg))

    if i > len(msg):
        flst.append(tmplst)
        i = 0
        tmplst = []
        jumpos+=1

    if len(msg) == jumpos:
        break
print(flst)

def decode(arr, lst, flst1, modified):

    print(lst)
    if len(arr) == 0:
        if modified:
            flst1.append(lst)
        return

    tmp1 = int(arr[0])
    if tmp1 != 0:

        tmplst = []
        if lst  and len(lst) > 0:
            tmplst = lst.copy()

        tmplst.append(tmp1)
        tmparr = arr[1:]
        decode(tmparr, tmplst, flst1, True)


    tmp2 = int(''.join(arr[0:2]))
    if tmp2 < 27:

        tmplst = []
        if lst and len(lst) > 0:
            tmplst = lst.copy()

        tmplst.append(tmp2)
        tmparr = arr[2:]
        decode(tmparr, tmplst, flst1, True)

flst1 = []
decode(['1','2'], None, flst1, False)
print(flst1)