try:
    # Kode yang berpotensi menimbulkan exception
    angka = int(input("Masukkan angka: "))
except ValueError:
    # Menangani exception ValueError
    print("Input tidak valid. Harap masukkan angka.")
except Exception as e:
    # Menangani exception lainnya
    print(f"Terjadi kesalahan: {e}")
else:
    # Dieksekusi jika tidak ada exception
    print(f"Angka yang dimasukkan: {angka}")
finally:
    # Selalu dieksekusi
    print("Proses selesai.")