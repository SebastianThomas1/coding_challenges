# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/equality-in-a-array
#
# Equalize the Array

from collections import Counter


def equalize_array(arr):
    counter = Counter(arr)
    _, highest_occurrence = counter.most_common(1)[0]
    return len(arr) - highest_occurrence


if __name__ == '__main__':
    print(equalize_array([3, 3, 2, 1, 3]))  # 2
