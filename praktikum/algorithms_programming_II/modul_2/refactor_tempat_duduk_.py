# Membuat meja dengan 2 baris dan 3 kolom
jumlah_baris = 2
jumlah_kolom = 3

meja = [["" for kolom in range(jumlah_kolom)] for baris in range(jumlah_baris)]


# Mengisi setiap kursi dengan nama orang
for baris in range(jumlah_baris):
    for kolom in range(jumlah_kolom):
        nama = input(f"Yang akan duduk di meja ({baris}, {kolom}): ")
        meja[baris][kolom] = nama


# Menampilkan isi meja
def display_output():
    print("----------")
    for baris in meja:
        print(" | ".join(baris))
    print("------------------------")


def main():
    display_output()


main()