# 42. Trapping Rain Water
#
# Given n non-negative integers representing an elevation map where the
# width of each bar is 1, compute how much water it can trap after
# raining.

from typing import List


def trap(height: List[int]) -> int:
    if not height:
        return 0

    left_max = [0] * len(height)
    left_max[0] = height[0]
    for idx in range(1, len(height)):
        left_max[idx] = max(left_max[idx - 1], height[idx])

    right_max = [0] * len(height)
    right_max[-1] = height[-1]
    for idx in range(len(height) - 2, -1, -1):
        right_max[idx] = max(right_max[idx + 1], height[idx])

    return sum(min(left_max[idx], right_max[idx]) - height[idx]
               for idx in range(len(height)))


if __name__ == '__main__':
    print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
    print(trap([4, 2, 0, 3, 2, 5]))  # 9
