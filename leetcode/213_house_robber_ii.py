# Sebastian Thomas (coding at sebastianthomas dot de)

# https://leetcode.com/problems/house-robber-ii/
#
# 213. House Robber II
#
# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed. All houses at this
# place are arranged in a circle. That means the first house is the
# neighbor of the last one. Meanwhile, adjacent houses have a security
# system connected, and it will automatically contact the police if two
# adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers nums representing the amount of
# money of each house, return the maximum amount of money you can rob
# tonight without alerting the police.

from typing import List


def rob_linear(nums: List[int]) -> int:
    last = 0
    current = 0
    for num in nums:
        last, current = current, max(last + num, current)

    return current


def rob(nums: List[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


if __name__ == '__main__':
    print(rob([2, 3, 2]))  # 3
    print(rob([1, 2, 3, 1]))  # 4
    print(rob([0]))  # 0
