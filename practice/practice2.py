import numpy as np

def LU_decomposition(A):
    n = len(A)
    L = np.eye(n)
    U = np.copy(A)

    for k in range(n-1):
        for i in range(k+1, n):
            # membuat matriks segituga bawah
            if U[k, k] == 0:
                raise ValueError("Pivot nol ditemukan. Faktorisasi LU tidak dapat dilakukan.")
            L[i, k] = U[i, k] / U[k, k]
            for j in range(k, n):
                # membuat segitiga atas
                U[i, j] -= L[i, k] * U[k, j]
    return L, U


def gauss_elimination(A, b):
    """
    menggunakan subtitusi bawah
    """
    A = A.astype(float)
    b = b.astype(float)
    n = len(b)
    for k in range(n-1):
        if A[k, k] == 0:
            for i in range(k+1, n):
                if A[i, k] != 0:
                    A[[k, i]] = A[[i, k]]
                    b[[k, i]] = b[[i, k]]
                    break
        for i in range(k+1, n):
            m = A[i, k] / A[k, k]
            A[i, k+1:] -= m * A[k, k+1:]
            b[i] -= m * b[k]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    return x

def partial_pivot(A, b):
    n = len(A)
    for k in range(n-1):
        # mencari indeks terbesar
        max_index = np.argmax(abs(A[k:, k])) + k
        if max_index != k:
            # tukar baris k dengan baris max_index
            A[[k, max_index]] = A[[max_index, k]]
            b[[k, max_index]] = b[[max_index, k]]
        for i in range(k+1, n):
            m = A[i, k] / A[k, k]
            A[i, k:] -= m * A[k, k:]
            b[i] -= m * b[k]


def back_subtitution(A, b):
    n = len(A)
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    return x


def gauss_elimination(A, b):
    partial_pivot(A, b)
    return back_subtitution(A, b)

if __name__ == "__main__":
    A = np.array([[1, 1, 0, 3],
         [2, 1, -1, 1],
         [3, -1, -1, 2],
         [-1, 2, 3, -1]])
    b = np.array([4, 1, -3, 4])
    # L, U = LU_decomposition(A)
    x = gauss_elimination(A, b)
    for i in x:
        print(i)
    
    
