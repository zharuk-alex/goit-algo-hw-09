def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    coins.sort(reverse=True)
    result = {}

    for coin in coins:
        coin_count = amount // coin
        amount -= coin_count * coin
        if coin_count > 0:
            result[coin] = coin_count

        if amount == 0:
            break

    return result


if __name__ == "__main__":
    print(find_coins_greedy(113))  #  {50: 2, 10: 1, 2: 1, 1: 1}
