# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/count-triplets-1
#
# Count Triplets

from collections import defaultdict


def count_triplets(arr, r):
    if len(arr) < 3:
        return 0

    counter = defaultdict(int)
    pair_counter = defaultdict(int)

    count = 0
    # traverse array from rear to avoid division
    for value in arr[::-1]:
        count += pair_counter[(r*value, r*r*value)]
        pair_counter[(value, r*value)] += counter[r*value]
        counter[value] += 1

    return count


if __name__ == '__main__':
    print(count_triplets([1, 2, 2, 4], 2))  # 2
    print(count_triplets([1, 3, 9, 9, 27, 81], 3))  # 6
    print(count_triplets([1, 5, 5, 25, 125], 5))  # 4
