def standard_multiply(A, B):
    n, m, p = len(A), len(B), len(B[0])
    C = [[0] * p for _ in range(n)]
    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]
    return C


def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))]
            for i in range(len(A))]


def subtract(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A))]
            for i in range(len(A))]


def strassen_square(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    m = n // 2
    A11 = [r[:m] for r in A[:m]]
    A12 = [r[m:] for r in A[:m]]
    A21 = [r[:m] for r in A[m:]]
    A22 = [r[m:] for r in A[m:]]
    B11 = [r[:m] for r in B[:m]]
    B12 = [r[m:] for r in B[:m]]
    B21 = [r[:m] for r in B[m:]]
    B22 = [r[m:] for r in B[m:]]

    M1 = strassen_square(add(A11, A22), add(B11, B22))
    M2 = strassen_square(add(A21, A22), B11)
    M3 = strassen_square(A11, subtract(B12, B22))
    M4 = strassen_square(A22, subtract(B21, B11))
    M5 = strassen_square(add(A11, A12), B22)
    M6 = strassen_square(subtract(A21, A11), add(B11, B12))
    M7 = strassen_square(subtract(A12, A22), add(B21, B22))

    C11 = add(subtract(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(subtract(add(M1, M3), M2), M6)

    return [C11[i] + C12[i] for i in range(m)] + \
           [C21[i] + C22[i] for i in range(m)]


def strassen_multiply(A, B):
    n = len(A)
    size = 1
    while size < n:
        size *= 2

    Ap = [row + [0] * (size - n) for row in A]
    Bp = [row + [0] * (size - n) for row in B]
    Ap += [[0] * size for _ in range(size - n)]
    Bp += [[0] * size for _ in range(size - n)]

    C = strassen_square(Ap, Bp)
    return [row[:n] for row in C[:n]]


def strassen_hybrid(A, B, threshold=2):
    n = len(A)

    if n <= threshold:
        return standard_multiply(A, B)

    m = n // 2
    A11 = [r[:m] for r in A[:m]]
    A12 = [r[m:] for r in A[:m]]
    A21 = [r[:m] for r in A[m:]]
    A22 = [r[m:] for r in A[m:]]
    B11 = [r[:m] for r in B[:m]]
    B12 = [r[m:] for r in B[:m]]
    B21 = [r[:m] for r in B[m:]]
    B22 = [r[m:] for r in B[m:]]

    M1 = strassen_hybrid(add(A11,A22), add(B11,B22), threshold)
    M2 = strassen_hybrid(add(A21,A22), B11, threshold)
    M3 = strassen_hybrid(A11, subtract(B12,B22), threshold)
    M4 = strassen_hybrid(A22, subtract(B21,B11), threshold)
    M5 = strassen_hybrid(add(A11,A12), B22, threshold)
    M6 = strassen_hybrid(subtract(A21,A11), add(B11,B12), threshold)
    M7 = strassen_hybrid(subtract(A12,A22), add(B21,B22), threshold)

    C11 = add(subtract(add(M1,M4),M5),M7)
    C12 = add(M3,M5)
    C21 = add(M2,M4)
    C22 = add(subtract(add(M1,M3),M2),M6)

    return [C11[i]+C12[i] for i in range(m)] +            [C21[i]+C22[i] for i in range(m)]


A = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
B = [[2,1,0,1], [1,2,1,0], [0,1,2,1], [1,0,1,2]]

assert strassen_hybrid(A, B, threshold=2) == standard_multiply(A, B)
assert strassen_hybrid(A, B, threshold=4) == standard_multiply(A, B)

print("All test cases passed!")
