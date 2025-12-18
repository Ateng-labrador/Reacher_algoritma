"""
8x_1 + 2x_2 - x_3 = 27
-3x_1 - 6x_2 + 4x_3 = 4
12x_1 + 2x_2 + 2x_3 = 6
"""
def faktorisasiLUPivot(A):
    n = len(A)

    for i in range(n):
        max_row = i
        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[max_row][i]):
                max_row = j
            A[i], A[max_row] = A[max_row], A[i]
            # buat segitiga atas
            for k in range(i, n):
                pass

def segitiga_atas(A):
    n = len(A)
    A = [row[:] for row in A]

    for i in range(n):
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
        A[i], A[max_row] = A[max_row], A[i]

        for k in range(i + 1, n):
            if A[i][i] != 0:
                m = A[k][i] / A[i][i]
                for j in range(i, n):
                    A[k][j] -= m*A[i][j]
    return A

def segitiga_bawah(A):
    n = len(A)
    A = [row[:] for row in A]

    for i in range(n - 1, -1, -1):
        max_row = i
        for k in range(0, i):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
        A[i], A[max_row] = A[max_row], A[i]
        for k in range(0, i):
            if A[i][i] != 0:
                m = A[k][i] / A[i][i]
                for j in range(0, n):
                    A[k][j] -= m*A[i][j]
    return A

if __name__ == "__main__":
    A = [[1, 4, 7],
         [2, 5, 8],
         [3, 6, 10]]
    x = segitiga_bawah(A)
    for i in x:
        print(i)