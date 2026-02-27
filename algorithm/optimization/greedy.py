import os
os.system('cls')


def get_value():
    while True:
        try:
            kembalian = int(input('Masukkan jumlah kembalian: '))
            if kembalian <= 0:
                print('Kembalian harus lebih dari 0')
                continue
            else:
                return kembalian
        except ValueError:
            print('Masukkan Nilai Angka Yang Benar!')


def greedy_tukar_pecahan(uang_kembalian, uang_pecahan):
    result = {}
    total_lembar_terpakai = 0

    for lembar_uang in uang_pecahan:
        if uang_kembalian >= lembar_uang:
            count = uang_kembalian // lembar_uang
            print(count)

            uang_kembalian -= count * lembar_uang
            print(uang_kembalian)

            result[lembar_uang] = count
            print(result)

            total_lembar_terpakai += count
            print(total_lembar_terpakai)

        print('---')
        555
    return result, total_lembar_terpakai


def display_output(result, total):

    for uang, lembar in result.items():
        print(f'{uang:<7} : {lembar} lembar')

    print(f'\nTotal uang terpakai: {total} lembar')


def main():
    uang_kembalian = get_value()

    uang_pecah = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

    result, total = greedy_tukar_pecahan(uang_kembalian, uang_pecah)

    display_output(result, total)


if __name__ == '__main__':
    main()