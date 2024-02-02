import numpy as numpy
import pandas as pd


def find_coins_greedy(amount):
    coins = [50, 20, 10, 5, 2, 1]
    result = {}

    for coin in coins:
        if amount == 0:
            break
        count = amount // coin
        amount -= coin*count
        if count:
            result[coin] = count

    return result


def find_min_coins(amount):
    coins = [50, 20, 10, 5, 2, 1]
    dp = [0] + [float('inf')] * amount
    for i in range(min(coins), amount+1):
        dp[i] = min([dp[i-coin] if i-coin >= 0 else float('inf')
                    for coin in coins]) + 1

    coin_count = dp[-1]
    i = amount
    result = {}

    while i > 0 and coin_count > 0:
        for coin in coins:
            if i - coin >= 0 and dp[i-coin] == coin_count - 1:
                result[coin] = result.get(coin, 0) + 1
                i -= coin
                coin_count -= 1
                break

    return result


results = []


for i in range(1, 26):
    results.append({"amount": i, "greedy": find_coins_greedy(
        i), "dynamic": find_min_coins(i)})


df = pd.DataFrame(results)

print(df.head(25))
