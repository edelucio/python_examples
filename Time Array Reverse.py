import random
import time

def performance():
    n = 1024
    array = []
    while n < 5000000:
        for r in range(n):
            i = random.randint(0, n)
            array.append(i)
        begin = float(time.time())
        array.reverse()
        end = float(time.time())
        print(n, ' ', (end - begin) * 1000000)
        n * 2

performance()