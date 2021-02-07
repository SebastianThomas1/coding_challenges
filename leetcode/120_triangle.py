# Sebastian Thomas (coding at sebastianthomas dot de)

# https://leetcode.com/problems/triangle/
#
# 120. Triangle
#
# Given a triangle array, return the minimum path sum from top to
# bottom.
#
# For each step, you may move to an adjacent number of the row below.
# More formally, if you are on index i on the current row, you may move
# to either index i or index i + 1 on the next row.

from typing import List


def minimum_total(triangle: List[List[int]]) -> int:
    for i in range(1, len(triangle)):
        triangle[i][0] += triangle[i - 1][0]
        for j in range(1, i):
            triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
        triangle[i][i] += triangle[i - 1][i - 1]

    return min(triangle[-1])


if __name__ == '__main__':
    print(minimum_total([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))  # 11
    print(minimum_total([[-10]]))  # -10
