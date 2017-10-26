import random
import time

# Lista


def criaLista(length):
    listaCriada = random.sample(range(length), length)

    return listaCriada

# Primeira Derivada


def firstDerivative(algebraicPolynomial):
    polynomialArrayLength = len(algebraicPolynomial)
    derivative = []
    expoent = 1
    for polynomial in range(len(algebraicPolynomial), 0, -1):
        if(polynomial < polynomialArrayLength):
            if(expoent - 1 > 0):
                derivative.append(
                    str(algebraicPolynomial[polynomial - 1] * expoent) + "X^" + str(expoent - 1))
            else:
                derivative.append(
                    str(algebraicPolynomial[polynomial - 1] * expoent))
            expoent += 1
    return list(reversed(derivative))

# Performance


def performance(n):
    resultado = []
    lista = criaLista(n)

    while n < 30:
        begin = float(time.time())
        lista = firstDerivative(lista)
        print(n)
        finish = float(time.time())
        resultado.append(str((finish - begin) * 1000000))

        n = n + 2
    return resultado


resultado = performance(1)
for elemento in resultado:
    print(elemento)
