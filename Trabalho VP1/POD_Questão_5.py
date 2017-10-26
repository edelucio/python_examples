import random
import time

# Lista


def criaLista(length):
    listaCriada = random.sample(range(length), length)

    return listaCriada

# Unique1


def unique1(alist):
    for i in range(len(alist)):
        for j in range(i + 1, len(alist)):
            if alist[i] == alist[j]:
                return False
    return True

# Unique2


def unique2(alist):
    temp = sorted(alist)
    for j in range(1, len(temp)):
        if alist[j - 1] == alist[j]:
            return False
    return True

# Performance


def performance(length, isUniqueOne):
    array = criaLista(length)
    begin = float(time.time())

    if isUniqueOne == True:
        result = unique1(array)
    else:
        result = unique2(array)

    end = float(time.time())
    print(round(end - begin, 2))
    print(result)


performance(28000, True)
performance(60000000, False)

'''
Para unique1:
Array com 10.000 posições, Tempo médio: 8 segundos
Array com 20.000 posições, Tempo médio: 27 segundos
Array com 28.000 posições, Tempo médio: 60 segundos

Para unique2:
Array com 10.000.000 posições, Tempo médio: 8 segundos
Array com 50.000.000 posições, Tempo médio: 27 segundos
Array com 60.000.000 posições, Erro de memória (MemoryError)
'''
