# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/list-comprehensions
#
# List Comprehensions

def coordinates(x, y, z, n):
    return [[i, j, k] for i in range(x + 1) for j in range(y + 1)
            for k in range(z + 1) if i + j + k != n]


if __name__ == '__main__':
    print(coordinates(1, 1, 1, 2))
    # [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
    print(coordinates(2, 2, 2, 2))
    # [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2],
    #  [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1],
    #  [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2],
    #  [2, 2, 0], [2, 2, 1], [2, 2, 2]]
