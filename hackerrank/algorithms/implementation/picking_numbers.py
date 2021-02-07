# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/picking-numbers
#
# Picking Numbers

from collections import Counter


def picking_numbers(a):
    counter = Counter(a)
    neighbor_counter = {
        key: value + counter[key + 1] if key + 1 in counter else value
        for key, value in counter.items()
        }

    return max(neighbor_counter.values())


if __name__ == '__main__':
    print(picking_numbers([4, 6, 5, 3, 3, 1]))  # 3
    print(picking_numbers([1, 2, 2, 3, 1, 2]))  # 5
