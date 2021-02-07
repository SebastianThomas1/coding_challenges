# 85. Maximal Rectangle
#
# Given a rows x cols binary matrix filled with 0's and 1's, find the
# largest rectangle containing only 1's and return its area.

from typing import List, Set, Tuple


def reduce(indices: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
    reduced_indices = set()
    for i, j in indices:
        broken = False
        for k, l in reduced_indices:
            if k <= i and l <= j:
                broken = True
                break
            elif i <= k and j <= l:
                reduced_indices.remove((k, l))
                reduced_indices.add((i, j))
                broken = True
                break
        if not broken:
            reduced_indices.add((i, j))

    return reduced_indices


def maximalRectangle(matrix: List[List[str]]) -> int:
    if not matrix or not matrix[0]:
        return 0

    m = len(matrix)
    n = len(matrix[0])
    ranges = [[None] * n for _ in range(m)]
    start_indices = [[set()] * n for _ in range(m)]

    # row 0:
    if matrix[0][0] == '1':
        ranges[0][0] = 0, 0
    for l in range(1, n):
        if matrix[0][l] == '1':
            ranges[0][l] = (ranges[0][l - 1][0] if ranges[0][l - 1] else l, 0)

    for k in range(1, m):
        if matrix[k][0] == '1':
            ranges[k][0] = (0, ranges[k - 1][0][1] if ranges[k - 1][0] else k)
        for l in range(1, n):
            if matrix[k][l] == '1':
                ranges[k][l] = (ranges[k][l - 1][0] if ranges[k][l - 1] else l,
                                ranges[k - 1][l][1] if ranges[k - 1][l] else k)

    # row 0:
    if matrix[0][0] == '1':
        start_indices[0][0] = {(0, 0)}
    for l in range(1, n):
        if matrix[0][l] == '1':
            start_indices[0][l] = (start_indices[0][l - 1]
                                   if start_indices[0][l - 1]
                                   else {(0, l)})

    for k in range(1, m):
        if matrix[k][0] == '1':
            start_indices[k][0] = (start_indices[k - 1][0]
                                   if start_indices[k - 1][0]
                                   else {(k, 0)})
        for l in range(1, n):
            if matrix[k][l] == '1':
                start_indices[k][l] \
                    = {(max(i, ranges[k][l][1]), j)
                       for (i, j) in start_indices[k][l - 1]} \
                    .union({(i, max(j, ranges[k][l][0]))
                            for (i, j) in start_indices[k - 1][l]})
                start_indices[k][l].add((k, l))
                start_indices[k][l] = reduce(start_indices[k][l])

    max_area = max(((k - i + 1)*(l - j + 1) for k in range(m) for l in range(n)
                   for i, j in start_indices[k][l]), default=0)

    return max_area


if __name__ == '__main__':
    print(maximalRectangle([['1', '0', '1', '0', '0'],
                            ['1', '0', '1', '1', '1'],
                            ['1', '1', '1', '1', '1'],
                            ['1', '0', '0', '1', '0']]))  # 6
    print(maximalRectangle([['1', '0', '1', '1', '0'],
                            ['1', '0', '1', '1', '1'],
                            ['1', '1', '1', '1', '1'],
                            ['1', '0', '0', '1', '0']]))  # 6
    print(maximalRectangle([['1', '0', '1', '1', '0'],
                            ['0', '0', '1', '1', '1'],
                            ['1', '1', '1', '1', '1'],
                            ['1', '0', '0', '1', '0']]))  # 6
    print(maximalRectangle([]))  # 0
    print(maximalRectangle([['0']]))  # 0
    print(maximalRectangle([['1']]))  # 1
    print(maximalRectangle([['0', '0']]))  # 0
    print(maximalRectangle([['0', '0', '0', '0', '0', '0', '1'],
                            ['0', '0', '0', '0', '1', '1', '1'],
                            ['1', '1', '1', '1', '1', '1', '1'],
                            ['0', '0', '0', '1', '1', '1', '1']]))  # 9
