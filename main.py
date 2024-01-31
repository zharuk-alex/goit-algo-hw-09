import timeit
from find_coins_greedy import find_coins_greedy
from find_min_coins import find_min_coins

values = [999, 9999, 999_999]
results = {}

for val in values:
    results[val] = {
        "greedy": [
            find_coins_greedy(val),
            timeit.timeit(lambda: find_coins_greedy(val), number=10),
        ],
        "dynamic": [
            find_min_coins(val),
            timeit.timeit(lambda: find_min_coins(val), number=10),
        ],
    }

table = "Amount | Algorithm | Coins | Time\n" + "-" * 50 + "\n"
for amount, methods in results.items():
    for method, values in methods.items():
        coins, time = values
        coins_str = ", ".join(f"{coin}: {count}" for coin, count in coins.items())
        table += f"{amount} | {method.capitalize()} | {coins_str} | {time:.6f}\n"

print(table)
