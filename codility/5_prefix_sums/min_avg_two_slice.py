# Sebastian Thomas (coding at sebastianthomas dot de)

# https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/
#
# MinAvgTwoSlice
#
# Find the minimal average of any slice containing at least two
# elements.
#
# A non-empty array A consisting of N integers is given. A pair of
# integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array
# A (notice that the slice contains at least two elements). The average
# of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided
# by the length of the slice. To be precise, the average equals
# (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).
#
# For example, array A such that:
#   A[0] = 4
#   A[1] = 2
#   A[2] = 2
#   A[3] = 5
#   A[4] = 1
#   A[5] = 5
#   A[6] = 8
# contains the following example slices:
#   - slice (1, 2), whose average is (2 + 2) / 2 = 2;
#   - slice (3, 4), whose average is (5 + 1) / 2 = 3;
#   - slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
# The goal is to find the starting position of a slice whose average is
# minimal.
#
# Write a function:
#   def solution(A)
# that, given a non-empty array A consisting of N integers, returns the
# starting position of the slice with the minimal average. If there is
# more than one slice with a minimal average, you should return the
# smallest starting position of such a slice.
#
# For example, given array A such that:
#   A[0] = 4
#   A[1] = 2
#   A[2] = 2
#   A[3] = 5
#   A[4] = 1
#   A[5] = 5
#   A[6] = 8
# the function should return 1, as explained above.
#
# Write an efficient algorithm for the following assumptions:
#   - N is an integer within the range [2..100,000];
#   - each element of array A is an integer within the range
#   [−10,000..10,000].

def prefix_sums(a):
    n = len(a)
    pref = [0]
    for k in range(1, n + 1):
        pref.append(pref[k - 1] + a[k - 1])
    return pref


def average_of_slice(k, l, pref):
    return (pref[l + 1] - pref[k]) / (l - k + 1)


def solution(a):
    # for every slice written as union of two slices,
    # it can be shown that the average of the union slice can be written
    # as a convex sum of the averages of the two part slices
    # so if the average slice of the union slice is lower
    # than the average one part slice, then the average of the other part
    # is even lower that the average of the union slice
    # since every slice of length at least four can be divided into two
    # slices of length at least 2, it therefore suffices to consider only
    # slices of length 2 and 3 to find the minimal average
    n = len(a)
    pref = prefix_sums(a)

    idx_of_min_avg = 0
    min_avg = average_of_slice(0, 1, pref)

    for k in range(1, n - 2):
        avg = average_of_slice(k, k + 1, pref)
        if avg < min_avg:
            idx_of_min_avg = k
            min_avg = avg
        avg = average_of_slice(k, k + 2, pref)
        if avg < min_avg:
            idx_of_min_avg = k
            min_avg = avg

    avg = average_of_slice(n - 2, n - 1, pref)
    if avg < min_avg:
        idx_of_min_avg = n - 2

    return idx_of_min_avg


if __name__ == '__main__':
    print(solution([4, 2, 2, 5, 1, 5, 8]))  # 1
    print(solution([1, 0, 1, 0]))  # 1
    print(solution([2, 0, 1, 2]))  # 1
