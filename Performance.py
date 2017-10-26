import random
import time

def performance(sort, scenario):
    rates = {}
    n = 10
    while n < 50000:
        numbers = scenario(n)
        now = time()
        sort(numbers)
        done = time()
        diff = (done - now) * 1000
        rates[n] = diff
        print(n, '\t', diff)
        n *= 2
    print("Done")
    return rates