# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/maximize-it
#
# Maximize it!

from itertools import product


def maximize_it(lists, m):
    return max(map(lambda elements:
               sum(element * element % m for element in elements) % m,
               product(*lists)))


if __name__ == '__main__':
    print(maximize_it([[5, 4], [7, 8, 9], [5, 7, 8, 9, 10]], 1000))
    # 206
