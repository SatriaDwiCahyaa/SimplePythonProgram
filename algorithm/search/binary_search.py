import os
os.system('cls')

def binarySearch(data_array, target_nilai):
    kiri = 0
    kanan = len(data_array) - 1

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2

        if data_array[tengah] == target_nilai:
            return tengah
        elif data_array[tengah] < target_nilai:
            kiri = tengah + 1
        else:
            kanan = tengah - 1

    return -1


def pemeriksa():
    data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 11

    hasil = binarySearch(data, target)

    if hasil != -1:
        print(f"{target} Ditemukan di indeks: ", hasil) 
    else:
        print(f"{target} tidak ditemukan")


def main():
    pemeriksa()
    input()


if __name__ == "__main__":
  main()