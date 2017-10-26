import random
import time

# Multiplos vetores


def multiplyArrays(arrayOne, arrayTwo):
    result = []
    for x in range(len(arrayOne) - 1):
        result.append(arrayOne[x] * arrayTwo[x])

    return result


# Lista aleatória
def criaLista(length):
    listaCriada = random.sample(range(length), length)
    return listaCriada

# Performance


def performance(n):
    resultado = []
    lista1 = criaLista(n)
    lista2 = criaLista(n)

    while n < 5000000:
        begin = float(time.time())
        lista3 = multiplyArrays(lista1, lista2)
        print(n)
        finish = float(time.time())
        resultado.append(str((finish - begin) * 1000000))

        n = n * 2
    return resultado


resultado = performance(1)
for elemento in resultado:
    print(elemento)
