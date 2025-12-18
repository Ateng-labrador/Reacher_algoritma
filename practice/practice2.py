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

    upper = [[0 for _ in range(n)]
             for _ in range(n)]
    lower = [[0 for _ in range(n)]
             for _ in range(n)]
    # ambil kolom
    # stay pada satu pivot
    for i in range(n):
        # ambil baris
        # ambil baris satu satu
        for k in range(i, n):
            sum = 0
            for j in range(i):
                for j in range(i):
                    sum += (lower[i][j] * upper[i][k])
            upper[i][k] = A[i][k] - sum
    return upper

if __name__ == "__main__":
    A = [[1, 4, 7],
         [2, 5, 8],
         [3, 6, 10]]
    n = len(A)

    upper = [[0 for _ in range(n)]
             for _ in range(n)]
    lower = [[0 for _ in range(n)]
             for _ in range(n)]
    # ambil kolom
    # stay pada satu pivot
    for i in range(n):
        # ambil baris
        # ambil baris satu satu
        for k in range(i, n):
            sum = 0
            for j in range(i):
                for j in range(i):
                    print(f"ini lower [{i}][{j}] = {lower[i][j]}")
                    print(f"ini upper [{i}][{j}] = {upper[i][j]}")
                    sum += (lower[i][j] * upper[i][k])
            print(f"ini upper [{i}][{k}] = {upper[i][k]}")
            print(f"{sum}")
            upper[i][k] = A[i][k] - sum
    print('\n')
    for row in upper:
        print(row)
    
