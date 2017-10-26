import random
import time

# Lista aleatória


def criaLista(length):
    listaCriada = random.sample(range(length), length)

    return listaCriada

# Invertendo Lista


def reverse(lista):
    i = 0  				# posição do primeiro elemento
    j = len(lista) - 1  # posição do último elemento
    aux = 0
    while i < j:
        aux = lista[i]
        lista[i] = lista[j]
        lista[j] = aux
        i += 1
        j -= 1
    return lista

# Performance


def performance(n, isNativa):
    resultado = []
    lista = criaLista(n)

    while n < 5000000:
        if(isNativa):
            begin = float(time.time())
            lista = list(reversed(lista))
        else:
            begin = float(time.time())
            lista = reverse(lista)

        finish = float(time.time())

        resultado.append(str((finish - begin) * 1000000))

        n = n * 2
    return resultado


resultado = performance(1024, False)
for elemento in resultado:
    print(elemento)
