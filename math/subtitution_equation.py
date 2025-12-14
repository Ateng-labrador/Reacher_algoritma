# back subtitution
# tipe data list
#*
# Syarat dalam algoritma ini
# matrik harus segitiga
# baik atas atau bawah
# 
# *#
def forward_subtitution(L, b):
    n = len(b)
    y = [0] * n

    for i in range(n):
        sum = b[i]
        for j in range(i):
            sum -= L[i][j] * y[j]
        y[i] = sum / L[i][i]
    return y

def backward_substitution(U, y):
    n = len(y)
    x = [0] * n
    for i in range(n-1, -1, -1):
        sum = y[i]
        for j in range(i+1, n):
            sum -= U[i][j] * x[j]
        x[i] = sum / U[i][i]
    return x
