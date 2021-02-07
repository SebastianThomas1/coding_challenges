# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/iterables-and-iterators
#
# Iterables and Iterators

from itertools import combinations
from math import factorial


def comb(n, k):
    return factorial(n) / (factorial(k)*factorial(n - k))


def probabilities_a(chars, k):
    occurrences = sum(1 for combination in combinations(chars, k)
                      if 'a' in combination)
    return occurrences / comb(len(chars), k)


if __name__ == '__main__':
    print(probabilities_a(['a', 'a', 'c', 'd'], 2))  # 0.833333333333333
