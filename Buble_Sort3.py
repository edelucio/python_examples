def sort3(A):
    n = len(A)
    k = n - 1
    for j in range(n):
        changes = False
        for i in range(k):
            if A[i] > A[i + 1]:
                tmp = A[i + 1]
                A[i + 1] = A[i]
                A[i] = tmp
                changes = True

            if i == k and A[i] < A[i + 1]:
                k = k - 1
        k = k - 1
        print(A)
        if not changes:
            print("There are no changes!!!")
            break
    return A

sort3([20, 12, 6, 4, 3, 22, 8, 15, 1, 2])
