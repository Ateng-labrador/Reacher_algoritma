import math

"""
Kaprekar number adalah sebuah bilangan dimana jika di kuadratkan
dan dibagi dua dan di jumlahkan dan maka akan menghasilkan bilangan-
nya kembali.
"""

def kaprkar_number(number):
    if number == 1:
        return True
    
    sq_n = number * number
    cout_digit = 0
    while not sq_n == 0:
        cout_digit += 1
        sq_n = sq_n // 10

    sq_n = number * number

    r_digits = 0
    while r_digits < cout_digit:
        r_digits += 1
        eq_parts = pow(10,r_digits)

        sum = sq_n // eq_parts + sq_n % eq_parts
        if sum == number:
            return True
    
    return False

