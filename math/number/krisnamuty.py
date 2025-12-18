from math import factorial

"""
1.  ambil setiap digit lalu lalu pisahkan
2.  lakukan factorial pada setiap digit
3.  jumlahkan setiap angka yang sudah di faktorialkan
4.  apakah sama dengan target jika sama maka benar
"""

def krishamurty(n):
    total = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        total += factorial(digit)
        temp = temp // 10
    return total == n

def list_krismurty(n):
    hasil = []

    for i in range(1,n+1):
        total = 0
        temp = i
        while temp > 0:
            digit = temp % 10
            total += factorial(digit)
            temp = temp // 10
        if total == i:
            hasil.append(i)
    return hasil

def cout_digit(n):
    total = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        total += digit
        temp = temp // 10
    return total

if __name__ == "__main__":
    print(list_krismurty(500))
