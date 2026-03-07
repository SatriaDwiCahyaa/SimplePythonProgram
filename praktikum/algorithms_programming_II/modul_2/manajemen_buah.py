buah_list = ["Mangga", "Pepaya", "Semangka", "Apple"]

def show_menu():
    print("========= MENU =========")
    print("[1] Show All Buah")
    print("[2] Insert Buah")
    print("[3] Edit Buah")
    print("[4] Delete Buah")
    print("[5] Exit")
    return input("PILIH MENU> ")


def show_all_buah():
    if not buah_list:
        print("Belum ada data")
    else:
        for i, buah in enumerate(buah_list):
            print(f"[{i}] {buah}")


def insert_buah():
    nama_buah = input("Nama buah: ")
    buah_list.append(nama_buah)


def edit_buah():
    show_all_buah()
    index = int(input("Pilih nomor buah: "))
    buah_list[index] = input("Nama baru: ")


def delete_buah():
    show_all_buah()
    index = int(input("Pilih nomor buah: "))
    buah_list.pop(index)
    while True:
        pilihan = show_menu()
        if pilihan == "1":
            show_all_buah()
        elif pilihan == "2":
            insert_buah()
        elif pilihan == "3":
            edit_buah()
        elif pilihan == "4":
            delete_buah()
        elif pilihan == "5":
            break
        else:
            print("Pilihan salah!")


def main():
    delete_buah()


if __name__ == "__main__":
    main()