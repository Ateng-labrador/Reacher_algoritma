def subtitusi_maju(L, b):
    """
    Algoritma ini bertujuan untuk mencari
    nilai y dari Ly = b.
    
    Parameter:
    L : Matriks segitiga bawah
    b : Matriks pada ruas kanan

    Return:
    y : nilai dari solusi
    """
    y = [0] * len(b)

    for i in range(len(b)):
        sum = b[i]
        for j in range(i):
            sum -= L[i][j] * y[j]
        y[i] = sum / L[i][i]
    return y


def subtitusi_mundur(U, y):
    """
    Algoritma ini bertujuan untuk mencari
    nilai x dengan menerima matriks segitiga
    Atas Ux = y

    Parameter:
    U : Matriks Segitiga Atas
    y : Matriks pada ruas kanan

    Return:
    x : nilai dari solusi
    """
    x = [0] * len(y)
    for i in range(len(y)-1, -1, -1):
        sum = y[i]
        for j in range(i+1, len(y)):
            sum -= U[i][j] * x[j]
        x[i] = sum / U[i][i]
    return x


if __name__ == "__main__":
    """
    Sistem: Ax = b
        ↓
    LU Decomposition
    A = L × U
        ↓
    Ax = b → (L×U)x = b
        ↓
    Step 1: Ly = b (Maju Substitution)
        ↓
    Step 2: Ux = y (Muncur Substitution)
        ↓
    Solusi: x
    
    """
    L = [
        [2, 0, 0],
        [1, 3, 0],
        [4, 2, 5]
    ]
    b = [4, 11, 29]
    U = [
        [2, 3, 1],
        [0, 4, 2],
        [0, 0, 5],
    ]
    y = subtitusi_maju(L, b)
    x = subtitusi_mundur(U, y)
    for i in x:
        print(i)
