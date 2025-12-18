def sumOfdigits_1(n):
    sum = 0
    while n > 0:
        # ambil digit terakhit
        last = n % 10
        # ambil setiap digit terakhir
        sum += last
        # hapus setiap digit terakhir
        n //= 10
    return sum


def sumOfDigits_2(n):
    if n == 0:
        return 0
    return n % 10 + sumOfDigits_2(n // 10)


def sumOfString(n):
    s = str(n)
    sum = 0
    for ch in s:
        sum += int(ch)
    return sum


if __name__ == "__main__":
    pass
