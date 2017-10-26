# Quebrar lista
def sort(list):
    if len(list) > 1:
        middle = len(list) // 2
        firstHalf = list[:middle]
        secondHalf = list[middle:]

        sort(firstHalf)
        sort(secondHalf)

        i = 0
        j = 0
        k = 0
        while i < len(firstHalf) and j < len(secondHalf):
            if firstHalf[i] < secondHalf[j]:
                list[k] = firstHalf[i]
                i = i + 1
            else:
                list[k] = secondHalf[j]
                j = j + 1
            k = k + 1
        while i < len(firstHalf):
            list[k] = firstHalf[i]
            i = i + 1
            k = k + 1
        while j < len(secondHalf):
            list[k] = secondHalf[j]
            j = j + 1
            k = k + 1
        return list

# Resultado eleição


def eleicao(list):
    list = sort(list)
    length = len(list)
    candidatoAtual = 0
    for i in range(length):
        if (i == length - 1) or (list[i] != list[i + 1]):
            result = (i - candidatoAtual) + 1
            candidatoAtual = i + 1
            print("Votos: " + str(result))
            print("Candidato: " + str(list[i]))


votos = [40, 13, 13, 45, 40, 13, 13, 45, 45, 20, 50, 50, 28, 13, 13, 45]
eleicao(votos)
print(votos)
