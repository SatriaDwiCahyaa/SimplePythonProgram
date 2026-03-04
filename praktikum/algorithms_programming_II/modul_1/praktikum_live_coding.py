import os
os.system('cls')


def main():

    banyak_data = int(input('Masukkan berapa angka yang ingin dimasukkan: '))

    total = 0

    for x in range(1, banyak_data + 1):
        nilai = float(input(f'Masukkan Angka {x}: '))
        total += nilai

    rata_rata = total / banyak_data


    print(f'Nilai rata-rata: {rata_rata:.2f}')

    input()


if __name__ == '__main__':
    main()