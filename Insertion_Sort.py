def insertion_sort(A):
    for k in range(1, len(A)):
        current = A[k]
        j = k

    while j > 0 and A[j - 1] > current:
        A[j] = A[j - 1]
        j -= 1

        A[j] = current
        print(k, A)

sequence = [25, 1, 4, 3, 3, 12, 2]

insertion_sort(sequence)
