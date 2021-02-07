# 122. Best Time to Buy and Sell Stock II
#
# Say you have an array prices for which the ith element is the price of
# a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as
# many transactions as you like (i.e., buy one and sell one share of the
# stock multiple times).
#
# Note: You may not engage in multiple transactions at the same time
# (i.e., you must sell the stock before you buy again).

from typing import List


def max_profit(prices: List[int]) -> int:
    if not prices:
        return 0

    profit = 0
    buy_price = prices[0]
    for idx, price in enumerate(prices):
        if idx < len(prices) - 1 and prices[idx + 1] < price:
            profit += max(price - buy_price, 0)
            buy_price = prices[idx + 1]

    profit += max(prices[-1] - buy_price, 0)

    return profit


if __name__ == '__main__':
    print(max_profit([7, 1, 5, 3, 6, 4]))  # 7
    print(max_profit([1, 2, 3, 4, 5]))  # 4
    print(max_profit([7, 6, 4, 3, 1]))  # 0
