def sort2(A):
    n = len(A)
    k = len(A) - 1
    for j in range(len(A)):
        for i in range(k):
            if A[i] > A[i + 1]:
                tmp = A[i + 1]
                A[i + 1] = A[i]
                A[i] = tmp
            if i == k and A[I] < A[I + 1]:
                K = K - 1
        k = k - 1
        print(A)
    return A

sort2([20, 12, 6, 4, 3, 22, 8, 15, 1, 2])
