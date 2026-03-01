import os
os.system('cls')

# ─────────────────────────────────────────────
# TUGAS 2: Menghitung Gaji Bersih (Pajak 5%)
# ─────────────────────────────────────────────

def gaji_bersih():
    print("=" * 45)
    print("   TUGAS 2 - MENGHITUNG GAJI BERSIH")
    print("=" * 45)

    PAJAK = 0.05  # Pajak 5%

    nama       = input("Nama Karyawan : ")
    gaji_kotor = float(input("Gaji Kotor (Rp): "))

    potongan_pajak = gaji_kotor * PAJAK
    gaji_bersih    = gaji_kotor - potongan_pajak

    print(f"\n{'─' * 40}")
    print(f"  Nama Karyawan  : {nama}")
    print(f"  Gaji Kotor     : Rp {gaji_kotor:,.0f}")
    print(f"  Potongan Pajak : Rp {potongan_pajak:,.0f} (5%)")
    print(f"  Gaji Bersih    : Rp {gaji_bersih:,.0f}")
    print(f"{'─' * 40}\n")

def main():
    gaji_bersih()

if __name__ == "__main__":
    main()