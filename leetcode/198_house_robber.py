# Sebastian Thomas (coding at sebastianthomas dot de)

# https://leetcode.com/problems/house-robber/
#
# 198. House Robber
#
# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint
# stopping you from robbing each of them is that adjacent houses have
# security system connected and it will automatically contact the police
# if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money
# of each house, determine the maximum amount of money you can rob
# tonight without alerting the police.

from typing import List


def rob(nums: List[int]) -> int:
    last = 0
    current = 0
    for num in nums:
        last, current = current, max(last + num, current)

    return current


if __name__ == '__main__':
    print(rob([1, 2, 3, 1]))  # 4
    print(rob([2, 7, 9, 3, 1]))  # 12
    print(rob([1, 2, 3, 4, 5, 6, 7]))  # 16
