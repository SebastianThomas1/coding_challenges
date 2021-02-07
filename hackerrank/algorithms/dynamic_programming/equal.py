# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/equal
#
# Equal

# The following dynamic programming approach yields a time out.
#
# PORTIONS = (1, 2, 5)
#
#
# def equal(arr, portions=PORTIONS):
#     length = len(arr)
#
#     minimal_value = min(arr)
#     # normalize arr
#     arr = [value - minimal_value for value in arr]
#
#     max_difference = max(arr) + max(portions) - 1
#
#     # min_counts[d] is in iteration idx the minimum number of portions
#     # needed to obtain an amount of d chocolates, using portions of
#     # sizes portions[:idx + 1]
#     min_counts = [0] + [float('inf')] * max_difference
#
#     for idx in range(len(portions)):
#         for d in range(max_difference, 0, -1):
#             # min_counts[d] is already the minimum number of portions
#             # if we do not include portions of size portions[idx]
#             # we can include at most d // portions[idx] portions of
#             # size portions[idx], and we take the count that minimizes
#             # the total count
#             min_counts[d] = min(
#                 min_counts[d - count*portions[idx]] + count
#                 for count in range(d // portions[idx] + 1))
#
#     return min(sum(min_counts[d + base] for d in arr)
#                for base in range(max(portions)))


def equal(arr):
    minimal_value = min(arr)
    # normalize arr
    arr = [value - minimal_value for value in arr]

    min_count = float('inf')
    for base in range(3):
        count = 0
        for value in arr:
            q, r = divmod(value + base, 5)
            count += q
            q, r = divmod(r, 2)
            count += q + r  # r == r // 1
        min_count = min(min_count, count)

    return min_count


if __name__ == '__main__':
    print(equal([8, 8, 8, 8]))  # 0
    print(equal([3, 3, 3, 8]))  # 1
    print(equal([2, 2, 3, 7]))  # 2
    print(equal([10, 7, 12]))  # 3
