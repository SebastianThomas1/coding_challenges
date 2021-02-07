# 63. Unique Paths II
#
# A robot is located at the top-left corner of a m x n grid (marked
# 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The
# robot is trying to reach the bottom-right corner of the grid (marked
# 'Finish' in the diagram below).
#
# Now consider if some obstacles are added to the grids. How many unique
# paths would there be?
#
# An obstacle and space is marked as 1 and 0 respectively in the grid.

from typing import List


def unique_paths_with_obstacles(obstacleGrid: List[List[int]]) -> int:
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    counts = [0] * n
    for j in range(n):
        if obstacleGrid[0][j]:
            break
        else:
            counts[j] = 1
    for i in range(1, m):
        if obstacleGrid[i][0]:
            counts[0] = 0
        for j in range(1, n):
            if obstacleGrid[i][j]:
                counts[j] = 0
            else:
                counts[j] += counts[j - 1]

    return counts[-1]


if __name__ == '__main__':
    print(unique_paths_with_obstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    # 2
    print(unique_paths_with_obstacles([[0, 1], [0, 0]]))  # 1
    print(unique_paths_with_obstacles([[1, 0]]))  # 0
    print(unique_paths_with_obstacles([[0, 0], [1, 1], [0, 0]]))  # 0
    print(unique_paths_with_obstacles([[0, 1, 0, 0, 0], [1, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))
    # 0
