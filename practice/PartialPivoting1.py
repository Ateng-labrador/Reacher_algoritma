"""
3x_1 - 0.1x_2 - 0.2x_3 = 7.85
0.1x_1 + 7x_2 - 0.3x_3 = -19.3
0.3x_1 + 0.2x_2 + 10x_3 = 71.4
"""
def algoritmagausspivot(A, b):
    n = len(b)
    A = [row[:] for row in A]
    b = b[:]

    for i in range(n):
        max_row = i
        for k in range(i + 1, n):
            if abs(A[i][k]) > abs(A[max_row][i]):
                max_row = k
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]
        for k in range(i + 1, n):
            if A[i][i] != 0:
                m = A[k][i] / A[i][i]
                for j in range(i, n):
                    A[k][j] -= m*A[i][j]
                b[k] -= m*b[i]
    return A, b

def subtitusi_mundur(U, y):
    n = len(y)
    x = [0] * n
    
    for i in range(n-1, -1, -1):
        sum =  y[i]
        for j in range(i + 1, n):
            sum -= U[i][j] * x[j]
        x[i] = sum / U[i][i]
    return x

if __name__ == "__main__":
    A = [
        [3, -0.1, -0.2],
        [0.1, 7, -0.3],
        [0.3, 0.2, 10],
    ]
    b = [7.85, -19.3, 71.4]
    U, y = algoritmagausspivot(A, b)
    x = subtitusi_mundur(U, y)
    
