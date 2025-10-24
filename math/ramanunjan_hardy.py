from array import array

"""
Taxi_cab(x):
1.  Buat array berisi kumpulkan kubik
2.  Buat dictionary untuk memuat sebuah nilai yang belum muncul
3.  Buat sebuah set() untuk menemukan sebuah angka ramanunnajn
4.  jika hasil penjumlahan belum pernah muncul maka masukkan kedalam
    dictionary,jika tidak maka masukkan kedalam set
"""

def taxi_cab(x):
    cubes = array('i',[i**3 for i in range(0,x)])
    dict_sum_pairs = {}
    raman = set()

    for a in range(0,x):
        for b in range(a+1,x):
            a3,b3 = cubes[a],cubes[b]

            sum_pairs = a3 + b3

            if sum_pairs not in dict_sum_pairs:
                dict_sum_pairs[sum_pairs] = (a,b)
            else:
                raman.add(sum_pairs)
    return sorted(raman)


def is_taxi_cab(x):
    MAX_NUMBER = 100
    cubes = array('i',[i**3 for i in range(0,MAX_NUMBER)])
    dict_sum_pairs = {}
    raman = set()

    for a in range(0,MAX_NUMBER):
        for b in range(a+1,MAX_NUMBER):
            a3,b3 = cubes[a],cubes[b]

            sum_pairs = a3 + b3

            if sum_pairs not in dict_sum_pairs:
                dict_sum_pairs[sum_pairs] = (a,b)
            else:
                raman.add(sum_pairs)

    return True if x in sorted(raman) else False
        


def main(args=None):
    print(taxi_cab(100))


if __name__ == "__main__":
    main()
