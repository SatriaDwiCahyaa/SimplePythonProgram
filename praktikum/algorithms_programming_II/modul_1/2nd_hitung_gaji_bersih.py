from colorama import Fore, Style
import os
os.system('cls')


# ─────────────────────────────────────────────
# TUGAS 2: Menghitung Gaji Bersih (Pajak 5%)
# ─────────────────────────────────────────────
def welcome_sign():
    print("=" * 45)
    print("   TUGAS 2 - MENGHITUNG GAJI BERSIH")
    print("=" * 45)


def get_valid_input(pesan_perintah, tipe_data):
    while True:
        try:
            user_input = input(pesan_perintah)

            # Jika tipe string
            if tipe_data == str:
                if user_input.strip() == "":
                    raise ValueError("Input tidak boleh kosong.")
                return user_input

            # Jika tipe float
            elif tipe_data == float:
                nilai = float(user_input)
                if nilai <= 0:
                    raise ValueError("Gaji tidak boleh negatif atau kosong.")
                return nilai

        except ValueError as e:
            print(
                Fore.RED + f"Error: {e}. Silakan coba lagi.\n", Style.RESET_ALL)


def gaji_bersih():

    PAJAK = 0.05  # Pajak 5%

    nama = get_valid_input("Nama Karyawan  : ", str)
    gaji_kotor = get_valid_input("Gaji Kotor (Rp): ", float)

    potongan_pajak = gaji_kotor * PAJAK
    gaji_bersih = gaji_kotor - potongan_pajak

    print(f"\n{'─' * 40}")

    print(f"  Nama Karyawan  : {nama}")
    print(f"  Gaji Kotor     : Rp {gaji_kotor:,.0f}")
    print(f"  Potongan Pajak : Rp {potongan_pajak:,.0f} (5%)")
    print(f"  Gaji Bersih    : Rp {gaji_bersih:,.0f}")

    print(f"{'─' * 40}\n")


def main():
    welcome_sign()
    gaji_bersih()


if __name__ == "__main__":
    main()
