# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
#
# Snail

def snail_indices(n):
    if n == 0:
        return []
    elif n == 1:
        return [(0, 0)]
    else:
        indices = []
        for j in range(n):
            indices.append((0, j))
        for i in range(1, n):
            indices.append((i, n - 1))
        for j in range(1, n):
            indices.append((n - 1, n - 1 - j))
        for i in range(1, n-1):
            indices.append((n - 1 - i, 0))
        return indices + [(i + 1, j + 1) for (i, j) in snail_indices(n - 2)]


def snail(matrix):
    if matrix == [[]]:
        return []
    else:
        return [matrix[i][j] for (i, j) in snail_indices(len(matrix))]


if __name__ == '__main__':
    print(snail([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]))  # [1, 2, 3, 6, 9, 8, 7, 4, 5]
    print(snail([[1, 2, 3],
                 [8, 9, 4],
                 [7, 6, 5]]))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
