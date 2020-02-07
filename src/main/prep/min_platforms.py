
arv = [2, 2.1, 3, 3.2, 3.5, 5]
dep = [2.3, 3.4, 3.2, 4.3, 4, 5.2]

arv = [9, 9.4, 9.5, 11, 15, 18]
dep = [9.1, 12, 11.2, 11.3, 19, 20]

arv = [9, 11, 12.35]
dep = [10, 12, 12.4]

cm = 0
mm = 0

tt = arv + dep
tt.sort()
print(tt)

for x in tt:

    if x in dep:
        cm -=1

    if x in arv:
        cm +=1

    if cm > mm:
       mm = cm

print(mm)

