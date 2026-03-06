import os
os.system('cls')

def binary_search(sumber_data, target_nilai):
    kiri = 0
    kanan = len(sumber_data) - 1

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2

        if sumber_data[tengah] == target_nilai:
            return tengah
        elif sumber_data[tengah] < target_nilai:
            kiri = tengah + 1
        else:
            kanan = tengah - 1

    return -1


def pemeriksa():
    data = sorted([21, 23, 34, 45, 76, 23]) # Ascending
    target = 45

    hasil = binary_search(data, target)

    if hasil != -1:
        print(f'{target} ditemukan pada indeks: {hasil}')
    else:
        print(f'{target} tidak ditemukan')

def main():
    pemeriksa()
    input()


if __name__ == "__main__":
    main()