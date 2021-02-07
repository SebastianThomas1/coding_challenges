# 123. Best Time to Buy and Sell Stock III
#
# Say you have an array for which the ith element is the price of a
# given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at
# most two transactions.
#
# Note: You may not engage in multiple transactions at the same time
# (i.e., you must sell the stock before you buy again).

from typing import List


def max_profit(prices: List[int]) -> int:
    # max profit is a dictionary with pairs as keys
    # for each key:
    # the first entry states whether we currently hold a stock
    # the second entry states how many transactions (buys) we have
    # made since it is impossible to be in hold state before the first
    # day, profit is initialised with -infinity
    profit = {
        (True, 1): -float('inf'),
        (False, 1): 0,
        (True, 2): -float('inf'),
        (False, 2): 0
    }

    for price in prices:
        # either keep being in not-hold state or sell with price today
        profit[False, 2] = max(profit[False, 2], profit[True, 2] + price)

        # either keep being in hold state or buy with price and add one
        # transaction
        profit[True, 2] = max(profit[True, 2], profit[False, 1] - price)

        # either keep being in not-hold state or sell with price today
        profit[False, 1] = max(profit[False, 1], profit[True, 1] + price)

        # either keep being in hold state or buy with price today
        profit[True, 1] = max(profit[True, 1], -price)

    return profit[False, 2]


if __name__ == '__main__':
    print(max_profit([3, 3, 5, 0, 0, 3, 1, 4]))  # 6
    print(max_profit([1, 2, 3, 4, 5]))  # 4
    print(max_profit([7, 6, 4, 3, 1]))  # 0
    print(max_profit([1]))  # 0
    print(max_profit([3, 3, 5, 0]))  # 2
