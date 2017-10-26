# Múltiplos Vetores
def multiplyArrays(arrayOne, arrayTwo):
    result = []
    for x in len(arrayOne) - 1:
        result.append(arrayOne[x] * arrayTwo[x])

    return result


arrayOne = [5, 4, 3, 1]
arrayTwo = [1, 5, 6, 3]
arrayThree = multiplyArrays(arrayOne, arrayTwo)

print arrayThree
