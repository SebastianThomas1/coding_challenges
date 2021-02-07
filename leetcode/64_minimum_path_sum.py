# 64. Minimum Path Sum
#
# Given a m x n grid filled with non-negative numbers, find a path from
# top left to bottom right, which minimizes the sum of all numbers along
# its path.
#
# Note: You can only move either down or right at any point in time.

from typing import List
from copy import copy


def min_path_sum(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])

    min_sums = copy(grid[0])
    for j in range(1, n):
        min_sums[j] += min_sums[j - 1]
    for i in range(1, m):
        min_sums[0] += grid[i][0]
        for j in range(1, n):
            min_sums[j] = min(min_sums[j - 1], min_sums[j]) + grid[i][j]

    return min_sums[-1]


if __name__ == '__main__':
    print(min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))  # 7
    print(min_path_sum([[1, 2, 3], [4, 5, 6]]))  # 12
