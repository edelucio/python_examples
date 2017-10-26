# Primeira derivada
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


algebraicPolynomial = [5, 2, 4, 3]
derivative = firstDerivative(algebraicPolynomial)
print(derivative)
