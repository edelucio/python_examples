def sort1(A):
    n = len(A)

    k = len(A) - 1
    for j in range(len(A)):
        for i in range(k):
            if A[i] > A[i + 1]:
                tmp = A[i + 1]
                A[i + 1] = A[i]
                A[i] = tmp
        k = k - 1
        print(A)
    return A

sort1([20, 12, 6, 4, 3, 22, 8, 15, 1, 2])
