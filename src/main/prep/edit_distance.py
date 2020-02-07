
from src.main.prep.counter import Counter

def insert(s1, s2, i):

    if len(s1) < len(s2):

        ts1 = s1[:i]
        ts2 = s2[i+1:]
        ts = ts1 + s2[i]+ ts2
        return ts, s2
    else:
        ts1 = s2[:i]
        ts2 = s1[i + 1:]
        ts = ts1 + s1[i] + ts2
        return ts, s1

def remove(s1, s2, i):

    if len(s1) > len(s2):

        ts1 = s1[:i]
        ts2 = s1[i+1:]
        ts = ts1 + ts2
        return ts, s2
    else:
        ts1 = s2[:i]
        ts2 = s2[i+1:]
        ts = ts1 + ts2
        return ts, s1

def replace(s1, s2, i):

    return s1[:i] + s2[i] + s1[i+1:], s2


def edit_distance(str1, str2, counter):

    if str1 == str2:
        return

    for i in range(len(str1)):

        if str1[i] != str2[i]:

            if len(str1) != len(str2):

                tmpstr1, tmpstr2 = insert(str1, str2, i)
                tmpcounter = None
                if counter is None:
                    tmpcounter = Counter(1)
                else:
                    tmpcounter = Counter(counter.get_count())
                if tmpstr1 == tmpstr2:
                    print(tmpstr1, tmpstr2, tmpcounter.increment().get_count())
                else:
                    edit_distance(tmpstr1, tmpstr2, tmpcounter.increment())


                tmpstr1, tmpstr2 = remove(str1, str2, i)
                tmpcounter2 = None
                if counter is None:
                    tmpcounter2 = Counter(1)
                else:
                    tmpcounter2 = Counter(counter.get_count())
                if tmpstr1 == tmpstr2:
                    print(tmpstr1, tmpstr2, tmpcounter2.increment().get_count())
                else:
                    edit_distance(tmpstr1, tmpstr2, tmpcounter2.increment())

            if str1 != str2 and len(str1) == len(str2):
                tmpstr1, tmpstr2 = replace(str1, str2, i)
                tmpcounter = None
                if counter is None:
                    tmpcounter = Counter(1)
                else:
                    tmpcounter = Counter(counter.get_count())
                if tmpstr1 == tmpstr2:
                    print(tmpstr1, tmpstr2, tmpcounter.increment().get_count())
                else:
                    edit_distance(tmpstr1, tmpstr2, tmpcounter.increment())

                tmpstr1, tmpstr2 = replace(str2, str1, i)
                tmpcounter = None
                if counter is None:
                    tmpcounter = Counter(1)
                else:
                    tmpcounter = Counter(counter.get_count())
                if tmpstr1 == tmpstr2:
                    print(tmpstr1, tmpstr2, tmpcounter.increment().get_count())
                else:
                    edit_distance(tmpstr1, tmpstr2, tmpcounter.increment())

c = Counter(0)
edit_distance('geek', 'gesek', c)
print(c.get_count())