def greedy_coin_change(amount, denominations):
    result = {}
    total_coins = 0

    for coin in denominations:
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            result[coin] = count
            total_coins += count

    return result, total_coins


def main():
    denominations = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
    
    amount = int(input("Masukkan jumlah kembalian: "))

    if amount <= 0:
        print("Jumlah harus lebih dari 0")
        return

    result, total = greedy_coin_change(amount, denominations)

    print("\nRincian kembalian:")
    for coin, count in result.items():
        print(f"{coin:<7} : {count} lembar")

    print(f"\nTotal uang terpakai: {total} lembar/koin")


if __name__ == "__main__":
    main()