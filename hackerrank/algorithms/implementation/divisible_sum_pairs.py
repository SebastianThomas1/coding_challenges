# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/divisible-sum-pairs
#
# Divisible Sum Pairs

from collections import Counter


def divisible_sum_pairs(k, ar):
    ar = [value % k for value in ar]

    counter = Counter(ar)

    res = 0
    for i in range(k // 2 + 1):
        if i != (k - i) % k:
            res += counter[i] * counter[(k - i) % k]
        else:  # i == (k - i) % k
            res += counter[i] * (counter[i] - 1) // 2

    return res


if __name__ == '__main__':
    print(divisible_sum_pairs(3, [1, 3, 2, 6, 1, 2]))  # 5
