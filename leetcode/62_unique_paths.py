# 62. Unique Paths
#
# A robot is located at the top-left corner of a m x n grid (marked
# 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The
# robot is trying to reach the bottom-right corner of the grid (marked
# 'Finish' in the diagram below).
#
# How many possible unique paths are there?

def uniquePaths(m: int, n: int) -> int:
    if m < n:
        m, n = n, m

    counts = [1] * n
    for _ in range(m - 1):
        for idx in range(1, n):
            counts[idx] += counts[idx - 1]

    return counts[-1]


if __name__ == '__main__':
    print(uniquePaths(3, 7))  # 28
    print(uniquePaths(3, 2))  # 3
    print(uniquePaths(7, 3))  # 28
    print(uniquePaths(3, 3))  # 6
