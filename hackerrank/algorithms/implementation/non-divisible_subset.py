# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/non-divisible-subset
#
# Non-divisible subset

from collections import Counter


def non_divisible_subset(k, s):
    s = [value % k for value in s]

    counter = Counter(s)

    res = 0
    for i in range(k // 2 + 1):
        if i != (k - i) % k:
            res += max(counter[i], counter[(k - i) % k])
        elif counter[i] > 0:  # i == (k - i) % k
            res += 1

    return res


if __name__ == '__main__':
    print(non_divisible_subset(3, [1, 7, 2, 4]))  # 3
    print(non_divisible_subset(4, [2, 2, 2, 2]))  # 1
    print(non_divisible_subset(7, [278, 576, 496, 727, 410, 124, 338, 149, 209,
                                   702, 282, 718, 771, 575, 436]))  # 11
