# 121. Best Time to Buy and Sell Stock
#
# You are given an array prices where prices[i] is the price of a given
# stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one
# stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If
# you cannot achieve any profit, return 0.

from typing import List


def max_profit(prices: List[int]) -> int:
    if not prices:
        return 0

    min_price = prices[0]
    profit = 0
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit


if __name__ == '__main__':
    print(max_profit([7, 1, 5, 3, 6, 4]))  # 5
    print(max_profit([7, 6, 4, 3, 1]))  # 0
    print(max_profit([2, 1, 2, 1, 0, 1, 2]))  # 2
