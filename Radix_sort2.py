import random
from math import log10
 
radix = 10
base = 1
X = [random.randint(0, 1000) for _ in range(100)]
 
for i in range(int(log10(max(X))+1)):
    bucket = [[] for _ in range(radix)]
    [bucket[int(x / base) % radix].append(x) for x in X]
    X = [x for l in bucket for x in l]
    base *= radix
print(X)
