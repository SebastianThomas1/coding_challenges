# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/migratory-birds
#
# Migratory Birds

from collections import Counter


def migratory_birds(arr):
    return sorted(Counter(arr).most_common(),
                  key=lambda x: (-x[1], x[0]))[0][0]


if __name__ == '__main__':
    print(migratory_birds([2, 2, 1, 1, 3]))  # 1
    print(migratory_birds([1, 4, 4, 4, 5, 3]))  # 4
    print(migratory_birds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]))  # 3
