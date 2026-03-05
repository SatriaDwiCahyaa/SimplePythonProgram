import os
os.system('cls')


def binary_search(sumber_data, target):
    kiri = 0
    kanan = len(sumber_data) - 1

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2

        if sumber_data[tengah] == target:
            return tengah 
        elif sumber_data[tengah] < target:
            kiri = tengah  + 1
        else:
            kanan = kanan - 1
    return -1


def pemeriksa():
    ascending_data = [12, 23, 26, 34, 45, 56, 67]
    target = 0

    hasil = binary_search(ascending_data, target)

    if hasil != -1:
        print(f'Data ditemukan di\n indeks\t: {hasil}\n {target}')
    else:
        print('Data tidak ditemukan')


def main():
    pemeriksa()
    input()


if __name__ == "__main__":
    main()