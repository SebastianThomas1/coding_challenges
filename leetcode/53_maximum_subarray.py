# Sebastian Thomas (coding at sebastianthomas dot de)

# https://leetcode.com/problems/maximum-subarray/
#
# 53. Maximum Subarray
#
# Given an integer array nums, find the contiguous subarray (containing
# at least one number) which has the largest sum and return its sum.

from typing import List


def max_subarray(nums: List[int]) -> int:
    current_sum = 0
    max_sum = None
    for value in nums:
        current_sum = max(current_sum + value, value)
        max_sum = max(max_sum, current_sum) if max_sum is not None \
            else current_sum
    return max_sum


if __name__ == '__main__':
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(max_subarray([1]))  # 1
    print(max_subarray([0]))  # 0
    print(max_subarray([-1]))  # -1
    print(max_subarray([-100000]))  # -100000
