# Procura máximo e mínimo
def findMaxAndMin(alist):
    maxElement = alist[0]
    minElement = alist[0]
    for i in range(1, len(alist)):
        if maxElement < alist[i]:
            maxElement = alist[i]
        elif minElement > alist[i]:
            minElement = alist[i]
    print(maxElement)
    print(minElement)


list = [1, 4, 27, 2, 9]
findMaxAndMin(list)
