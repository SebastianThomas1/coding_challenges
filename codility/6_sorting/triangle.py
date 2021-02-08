# Sebastian Thomas (coding at sebastianthomas dot de)

# https://app.codility.com/programmers/lessons/6-sorting/triangle/
#
# Triangle
#
# Determine whether a triangle can be built from a given set of edges.
#
# An array A consisting of N integers is given. A triplet (P, Q, R) is
# triangular if 0 ≤ P < Q < R < N and:
#   - A[P] + A[Q] > A[R],
#   - A[Q] + A[R] > A[P],
#   - A[R] + A[P] > A[Q].
#
# For example, consider array A such that:
#   A[0] = 10    A[1] = 2    A[2] = 5
#   A[3] = 1     A[4] = 8    A[5] = 20
# Triplet (0, 2, 4) is triangular.
#
# Write a function:
#   def solution(A)
# that, given an array A consisting of N integers, returns 1 if there
# exists a triangular triplet for this array and returns 0 otherwise.
#
# For example, given array A such that:
#   A[0] = 10    A[1] = 2    A[2] = 5
#   A[3] = 1     A[4] = 8    A[5] = 20
# the function should return 1, as explained above. Given array A such
# that:
#   A[0] = 10    A[1] = 50    A[2] = 5
#   A[3] = 1
# the function should return 0.
#
# Write an efficient algorithm for the following assumptions:
#
#   - N is an integer within the range [0..100,000];
#   - each element of array A is an integer within the range
#     [−2,147,483,648..2,147,483,647].

def solution(a):
    n = len(a)
    a.sort()
    for k in range(n - 2):
        if a[k] + a[k + 1] > a[k + 2]:
            return 1
    return 0


if __name__ == '__main__':
    print(solution([10, 2, 5, 1, 8, 20]))  # 1
    print(solution([10, 50, 5, 1]))  # 0
