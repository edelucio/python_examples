import math


def create_buckets(base):
    buckets = []
    for i in range(base):
        buckets.append([])

        return buckets


def sort(items, base):
    tmp = -1
    j = 0

    m = int(math.log(items[0], base)) + 1

    while j < m:
        buckets = create_buckets(base)

        for number in items:
            tmp = number / math.pow(base, j)
            digit = int(tmp % base)
            buckets[digit].append(number)

        # print (buckets)

        a = 0
        for bucket in buckets:
            for i in bucket:
                items[a] = i
                a += 1
        print(items)

        j = j + 1


def sort_base10(items):
    sort(items, 10)


def sort_base2(items):
    sort(items, 2)


import random


def median_case(n):
    result = []
    for i in range(n):
        j = random.randint(10000, 99000)
        result.append(j)

    return result


from time import time


def performance(sort, scenario):
    rates = {}
    n = 10

    while n < 30000:
        numbers = scenario(n)

        now = time()
        sort(numbers)
        done = time()

        diff = (done - now) * 1000000

        rates[n] = diff

        print(n, '\t', diff)

        n *= 2

    print("Done")
    return rates


performance(sort_base10, median_case)
