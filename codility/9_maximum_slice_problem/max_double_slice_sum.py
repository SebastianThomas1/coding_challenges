# Sebastian Thomas (coding at sebastianthomas dot de)

# https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_double_slice_sum/
#
# MaxDoubleSliceSum
#
# Find the maximal sum of any double slice.
#
# A non-empty array A consisting of N integers is given.
#
# A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double
# slice.
#
# The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2]
# + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].
#
# For example, array A such that:
#   A[0] = 3
#   A[1] = 2
#   A[2] = 6
#   A[3] = -1
#   A[4] = 4
#   A[5] = 5
#   A[6] = -1
#   A[7] = 2
# contains the following example double slices:
#   - double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
#   - double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
#   - double slice (3, 4, 5), sum is 0.
# The goal is to find the maximal sum of any double slice.
#
# Write a function:
#   def solution(A)
# that, given a non-empty array A consisting of N integers, returns the
# maximal sum of any double slice.
#
# For example, given:
#   A[0] = 3
#   A[1] = 2
#   A[2] = 6
#   A[3] = -1
#   A[4] = 4
#   A[5] = 5
#   A[6] = -1
#   A[7] = 2
# the function should return 17, because no double slice of array A has
# a sum of greater than 17.
#
# Write an efficient algorithm for the following assumptions:
#   - N is an integer within the range [3..100,000];
#   - each element of array A is an integer within the range
#     [−10,000..10,000].

def solution(a):
    n = len(a)

    max_slice_sums_ending = [0]
    for idx in range(1, n - 2):
        max_slice_sums_ending.append(
            max(0, max_slice_sums_ending[-1] + a[idx]))

    max_slice_sums_starting = [0]  # use reverse order
    for idx in range(n - 2, 1, -1):
        max_slice_sums_starting.append(
            max(0, max_slice_sums_starting[-1] + a[idx]))

    max_double_slice_sum = 0
    for idx in range(len(max_slice_sums_ending)):
        max_double_slice_sum = max(max_double_slice_sum,
                                   max_slice_sums_ending[idx] +
                                   max_slice_sums_starting[-1 - idx])

    return max_double_slice_sum


if __name__ == '__main__':
    print(solution([3, 2, 6, -1, 4, 5, -1, 2]))  # 17
    print(solution([-1, 3, 2, 6, -1, 4, 5, -1, 2]))  # 20
    print(solution([3, 2, -6, 4, 0]))  # 6
    print(solution([-8, 10, 20, -5, -7, -4]))  # 30
    print(solution([5, 5, 5]))  # 0
