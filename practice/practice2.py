"""
8x_1 + 2x_2 - x_3 = 27
-3x_1 - 6x_2 + 4x_3 = 4
12x_1 + 2x_2 + 2x_3 = 6
"""
def faktorisasiLUPivot(A):
    n = len(A)
    lower = [[0 for _ in range(n)]
             for _ in range(n)]
    upper = [[0 for _ in range(n)]
             for _ in range(n)]
    for i in range(n):
        max_row = i
        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[max_row][i]):
                max_row = j
            A[i], A[max_row] = A[max_row], A[i]

            for k in range(i + 1, n):
                if lower[i][i] != 0:
                    m = lower[k][i] / lower[i][i]
                    for j in range(i, n):
                        lower[k][j] -= m*lower[i][j]

            for k in range(0, i):
                if A[i][i] != 0:
                    m = upper[k][i] / upper[i][i]
                    for j in range(0, n):
                        upper[k][j] -= m*upper[i][j]

    return lower, upper


# ...existing code...
def faktorisasiLUPivot_1(A):
    n = len(A)
    # salin A supaya tidak mengubah input asli
    M = [row[:] for row in A]
    # Inisialisasi
    L = [[0.0]*n for _ in range(n)]
    U = [[0.0]*n for _ in range(n)]
    P = list(range(n))  # representasi permutasi sebagai list indeks

    for i in range(n):
        # pivot parsial: cari baris dengan nilai maksimum pada kolom i
        max_row = i
        max_val = abs(M[i][i])
        for r in range(i+1, n):
            if abs(M[r][i]) > max_val:
                max_val = abs(M[r][i])
                max_row = r
        if max_row != i:
            M[i], M[max_row] = M[max_row], M[i]
            P[i], P[max_row] = P[max_row], P[i]
            # juga tukar baris L yang sudah terisi (kolom < i)
            for k in range(i):
                L[i][k], L[max_row][k] = L[max_row][k], L[i][k]

        # Doolittle: isi U baris i dan L kolom i
        if abs(M[i][i]) < 1e-12:
            raise ZeroDivisionError("Pivot numerik nol (atau sangat kecil). Matriks singular atau perlu pivoting lebih kuat.")

        # U[i,j]
        for j in range(i, n):
            s = 0.0
            for k in range(i):
                s += L[i][k]*U[k][j]
            U[i][j] = M[i][j] - s

        # L[j,i]
        L[i][i] = 1.0
        for j in range(i+1, n):
            s = 0.0
            for k in range(i):
                s += L[j][k]*U[k][i]
            L[j][i] = (M[j][i] - s) / U[i][i]

    return P, L, U

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
    P, L, U = faktorisasiLUPivot_1(A)
    for i in P:
        print(i)
    print("\n")
    for i in L:
        print(i)
    print("\n")
    for i in U:
        print(i)
    print("\n")
    atas = segitiga_atas(A)
    bawah = segitiga_bawah(A)
    print("matriks bawah")
    for i in bawah:
        print(i)
    print("\n")
    print("matriks atas")
    for i in atas:
        print(i)
    # print("\n")
    # lower, upper = faktorisasiLUPivot(A)
    # print("hasil dari faktorisasi bawah : ")
    # for i in lower:
    #     print(i)
    # print("\n")
    # print("hasil dari faktorisasi atas : ")
    # for i in upper:
    #     print(i)