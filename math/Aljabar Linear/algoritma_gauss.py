def algoritm_gauss_pivot(A, b):
    """
    Algoritma ini belum mendapatkan nilai x
    algoritma ini hanya membuat matriks A
    menjadi segitiga dan b menjadi matrik
    mengikuti matriks ruas kiri menggunakan pivot.
    
    """
    n = len(b)
    A = [row[:] for row in A]
    b = b[:]

    for i in range(n):
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]

        for k in range(i + 1, n):
            if A[i][i] != 0:
                m = A[k][i] / A[i][i]
                for j in range(i, n):
                    A[k][j] -= m * A[i][j]
                b[k] -= m * b[i]
    return A, b


def algoritma_gauss(A, b):
    """
    Algoritma gauss melakukan transformasi
    mengubah matrisk menjadi matrik segitga
    dan mengubah pada sisi kanannya juga.

    Parameter:
    A : Matriks (n x n)
    b : Matriks (n x 1)

    return:
    U : matriks segitiga atas
    b : matriks modifikasi
    """
    U = [row[:] for row in A]
    b = b[:]
    
    for i in range(len(b)):
        for k in range(i + 1, len(b)):
            if A[i][i] != 0:
                m = A[k][i] / A[i][i]
                for j in range(i, len(b)):
                    A[k][j] -= m * A[i][j]
                b[k] -= m * b[i]
    return U, b


def luDecomposition(mat):
    """
    Algoritma untuk membuat matriks segitiga
    dari sebuah matrik,memfaktor kan menjadi
    2 matrik matriks atas dan matriks bawah
    """
    n = len(mat)
    # lower = [[0], 0] * n
    # upper = [[0], 0] * n
    
    lower = [[0 for _ in range(n)]
             for _ in range(n)]
    upper = [[0 for _ in range(n)]
             for _ in range(n)]

    for i in range(n):
        # pembuatan pada bagian upper
        for k in range(i, n):
            sum = 0
            for j in range(i):
                sum += (lower[i][j] * upper[i][k])
            upper[i][k] = mat[i][k] - sum
        # pembuatan pada bagian lower
        for k in range(i, n):
            if(i == k):
                lower[i][i] = 1
            else:
                sum = 0
                for j in range(i):
                    sum += (lower[k][j] * upper[j][i])
                lower[k][i] = int((mat[k][i] - sum) /
                                  upper[i][i])  
    return lower, upper


def forward_subtitution(L, b):
    n = len(b)
    y = [0] * n

    for i in range(n):
        sum = b[i]
        for j in range(i):
            sum -= L[i][j] * y[j]
        y[i] = sum / L[i][i]
    return y


# def sumofdigit(n):
#     sum = 0
#     while n != 0:
#         last = n % 10
#         sum += last
#         n //= 10
#     return sum

if __name__ == "__main__":
    A = [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 10],
    ]
    b = [1, 2, 3]
    U, b = algoritma_gauss(A, b)
    for i in U:
        print(i)
    for i in b:
        print(b)