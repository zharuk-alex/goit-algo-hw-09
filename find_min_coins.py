def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    coins = [50, 25, 10, 5, 2, 1]
    min_coins = [float("inf")] * (amount + 1)
    min_coins[0] = 0
    coin_count = {coin: 0 for coin in coins}
    result = {}

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_count[i] = coin

    if min_coins[amount] == float("inf"):
        return None

    while amount > 0:
        coin = coin_count[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return result


if __name__ == "__main__":
    print(find_min_coins(113))  #  {50: 2, 10: 1, 2: 1, 1: 1}
