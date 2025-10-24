"""
happy number adalah sebuah bilanagn yang dimana jika setiap
digit di kuadratkan lalu di jumlahkan dan terus hingga mendapatkan
1 itu merupaka angka happy
"""

def sumDigit(n):
    total = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        total += digit * digit
        temp = temp // 10
    return total

def happy_or_sad(number):
    seen_number = set()

    while number > 1 and number not in seen_number:
        seen_number.add(number)
        number = sumDigit(number)
    return number == 1