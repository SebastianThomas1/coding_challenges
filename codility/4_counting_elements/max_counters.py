# Sebastian Thomas (coding at sebastianthomas dot de)

# https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/
#
# MaxCounters
#
# Calculate the values of counters after applying all alternating
# operations: increase counter by 1; set value of all counters to
# current maximum.
#
# You are given N counters, initially set to 0, and you have two
# possible operations on them:
#   - increase(X) − counter X is increased by 1,
#   - max counter − all counters are set to the maximum value of any
#                   counter.
#
# A non-empty array A of M integers is given. This array represents
# consecutive operations:
#   - if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
#   - if A[K] = N + 1 then operation K is max counter.
# For example, given integer N = 5 and array A such that:
#   A[0] = 3
#   A[1] = 4
#   A[2] = 4
#   A[3] = 6
#   A[4] = 1
#   A[5] = 4
#   A[6] = 4
# the values of the counters after each consecutive operation will be:
#   (0, 0, 1, 0, 0)
#   (0, 0, 1, 1, 0)
#   (0, 0, 1, 2, 0)
#   (2, 2, 2, 2, 2)
#   (3, 2, 2, 2, 2)
#   (3, 2, 2, 3, 2)
#   (3, 2, 2, 4, 2)
# The goal is to calculate the value of every counter after all
# operations.
#
# Write a function:
#   def solution(N, A)
# that, given an integer N and a non-empty array A consisting of M
# integers, returns a sequence of integers representing the values of
# the counters.
#
# Result array should be returned as an array of integers.
#
# For example, given:
#   A[0] = 3
#   A[1] = 4
#   A[2] = 4
#   A[3] = 6
#   A[4] = 1
#   A[5] = 4
#   A[6] = 4
# the function should return [3, 2, 2, 4, 2], as explained above.
#
# Write an efficient algorithm for the following assumptions:
#   - N and M are integers within the range [1..100,000];
#   - each element of array A is an integer within the range [1..N + 1].

from collections import Counter


def solution(n, a):
    max_indices = [idx for idx, X in enumerate(a) if X == n + 1]
    max_indices = [-1] + max_indices

    sum_of_maxima = 0
    for idx in range(len(max_indices) - 1):
        counter = Counter(a[max_indices[idx] + 1:max_indices[idx + 1]])
        if counter:
            _, maximum = counter.most_common(1).pop()
            sum_of_maxima += maximum

    total_counts = n * [sum_of_maxima]

    counter = Counter(a[max_indices[-1] + 1:])
    for idx, count in counter.items():
        total_counts[idx - 1] += count

    return total_counts


if __name__ == '__main__':
    print(solution(5, [3, 4, 4, 6, 1, 4, 4]))  # [3, 2, 2, 4, 2]
    print(solution(5, [3, 4, 4, 6, 6, 1, 4, 4]))  # [3, 2, 2, 4, 2]
    print(solution(5, [3, 4, 4, 6, 1, 6, 4, 4]))  # [3, 3, 3, 5, 3]
    print(solution(5, [3, 4, 4, 1, 4, 4]))  # [1, 0, 1, 4, 0]
    print(solution(5, [6, 3, 4, 4, 1, 4, 4]))  # [1, 0, 1, 4, 0]
    print(solution(5, [3, 4, 4, 1, 4, 4, 6]))  # [4, 4, 4, 4, 4]
    print(solution(5, [6, 3, 4, 4, 1, 4, 4, 6]))  # [4, 4, 4, 4, 4]
    print(solution(5, [6, 3, 4, 4, 6, 1, 4, 4]))  # [3, 2, 2, 4, 2]
    print(solution(5, [6, 6, 6]))  # [0, 0, 0, 0, 0]
