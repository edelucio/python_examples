from time import time

# Posição máxima


def select_max(A, left, right):
    max_pos = left
    i = left
    while i <= right:
        if A[i] > A[max_pos]:
            max_pos = i
        i = i + 1
    return max_pos

# Selection Sort


def selection_sort(A):
    for i in range(len(A) - 1, 0, -1):
        max_pos = select_max(A, 0, i)
        if max_pos != i:
            tmp = A[i]
            A[i] = A[max_pos]
            A[max_pos] = tmp

# Insertion Sort


def insertion_sort(A):
    for k in range(1, len(A)):
        current = A[k]
        j = k
        while j > 0 and A[j - 1] > current:
            A[j] = A[j - 1]
            j -= 1
            A[j] = current

# Performance


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
        print(n)
        print(diff)
        n *= 2
    print("Done")
    return rates

# Melhor caso


def best_case(n):
    r = range(n)
    return list(r)

# Pior caso


def worst_case(n):
    r = range(n)
    array = list(r)
    return array[::-1]


rates = performance(insertion_sort, best_case)

'''
10 0.010967254638671875
20 0.0171661376953125
40 0.026941299438476562
80 0.049114227294921875
160 0.09298324584960938
320 0.18787384033203125
640 0.392913818359375
1280 0.8101463317871094
2560 1.6422271728515625
5120 3.4248828887939453
10240 6.849050521850586
20480 14.93215560913086
40960 32.08279609680176
Done
'''

rates = performance(insertion_sort, worst_case)

'''
10 0.0209808349609375
20 0.062465667724609375
40 0.2422332763671875
80 0.9760856628417969
160 3.918170928955078
320 15.39921760559082
640 57.515621185302734
1280 190.7036304473877
2560 833.8003158569336
5120 3516.435146331787
10240 13610.971450805664
20480 60448.63152503967
40960 219413.84148597717
Done
'''

rates = performance(selection_sort, best_case)

'''
10 0.021696090698242188
20 0.05745887756347656
40 0.20194053649902344
80 0.7572174072265625
160 3.0786991119384766
320 11.90042495727539
640 47.68776893615723
1280 100.64530372619629
2560 392.3838138580322
5120 1780.1775932312012
10240 6566.65825843811
20480 26894.315719604492
40960 105962.4536037445
Done
'''

rates = performance(selection_sort, worst_case)

'''
10 0.014543533325195312
20 0.0457763671875
40 0.1537799835205078
80 0.6766319274902344
160 2.658843994140625
320 7.010698318481445
640 26.10611915588379
1280 91.33005142211914
2560 376.99389457702637
5120 1546.7519760131836
10240 6245.815992355347
20480 25974.810361862183
40960 107808.76016616821
Done

Worst case on selection_sort is better at performance rates
'''
