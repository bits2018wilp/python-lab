
import time

def rand7():

    t = int(time.time_ns())
    print(t)
    return (t%7)+1

for i in range(10):
    print(rand7())