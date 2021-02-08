# Sebastian Thomas (coding at sebastianthomas dot de)

# https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/
#
# 1326. Minimum Number of Taps to Open to Water a Garden

from typing import List


def min_taps(n: int, ranges: List[int]) -> int:
    # in iteration idx: min_actives[j] is minimum number of active
    # fountains to water the garden up to position j (included)
    min_actives = [float('inf')] * (n + 1)

    for idx in range(n + 1):
        left_idx = max(idx - ranges[idx], 0)
        right_idx = min(idx + ranges[idx], n)
        min_actives_left = min_actives[left_idx] if left_idx > 0 else 0
        for j in range(left_idx, right_idx + 1):
            # min_actives[j] is already the minimum number of active
            # fountains if we do not include fountain idx
            min_actives[j] = min(min_actives[j], min_actives_left + 1)

    return min_actives[-1] if min_actives[-1] < float('inf') else -1


if __name__ == '__main__':
    print(min_taps(5, [3, 4, 1, 1, 0, 0]))  # 1
    print(min_taps(3, [0, 0, 0, 0]))  # -1
    print(min_taps(7, [1, 2, 1, 0, 2, 1, 0, 1]))  # 3
    print(min_taps(8, [4, 0, 0, 0, 0, 0, 0, 0, 4]))  # 2
    print(min_taps(8, [4, 0, 0, 0, 4, 0, 0, 0, 4]))  # 1
