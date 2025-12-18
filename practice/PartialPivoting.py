"""
 0.0003X + 3.0000Y =  2.0001
 1.0000X + 1.0000Y =  1.0000
 Carilah solusi dari persamaan ini
"""

def algoritmaGaussPivot(A, b):
    n = len(b)
    A = [row[:] for row in A]
    b = b[:]

    # Ambil kolom
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
                    A[k][j] -= m*A[i][j]
                b[k] -= m * b[i]
    return A, b


def subtitusi_maju():
    pass


def subtitusi_mundur(U, y):
    n = len(y)
    x = [0] * n
    # kolom
    for i in range(n-1, -1, -1):
        sum = y[i]
        # baris
        for j in range(i + 1, n):
            sum -= U[i][j] * x[j]
        x[i] = sum / U[i][i]
    return x



if __name__ == "__main__":
    # A = [[0.0003, 3.0000],
    #      [1.0000, 1.0000]]
    A = [
        [1, 4, 7],
         [2, 5, 8],
         [3, 6, 10]
        ]
    b = [2.0001, 1.0000, 3.000]
    U, y = algoritmaGaussPivot(A, b)
    for row in U:
        print(row)
    # for row in y:
    #     print(row)
    # print('\n')
    # x = subtitusi_mundur(U, y)
    # print(x)
    