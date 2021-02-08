# Sebastian Thomas (coding at sebastianthomas dot de)

# https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/
#
# PermCheck
#
# Check whether array A is a permutation.
#
# A non-empty array A consisting of N integers is given.
#
# A permutation is a sequence containing each element from 1 to N once,
# and only once.
#
# For example, array A such that:
#   A[0] = 4
#   A[1] = 1
#   A[2] = 3
#   A[3] = 2
# is a permutation, but array A such that:
#   A[0] = 4
#   A[1] = 1
#   A[2] = 3
# is not a permutation, because value 2 is missing.
#
# The goal is to check whether array A is a permutation.
#
# Write a function:
#   def solution(A)
# that, given an array A, returns 1 if array A is a permutation and 0 if
# it is not.
#
# For example, given array A such that:
#   A[0] = 4
#   A[1] = 1
#   A[2] = 3
#   A[3] = 2
# the function should return 1.
#
# Given array A such that:
#   A[0] = 4
#   A[1] = 1
#   A[2] = 3
# the function should return 0.
#
# Write an efficient algorithm for the following assumptions:
#   - N is an integer within the range [1..100,000];
#   - each element of array A is an integer within the range
#     [1..1,000,000,000].

def solution(a):
    n = len(a)
    values = set(range(1, n + 1))
    for entry in a:
        if entry in values:
            values.remove(entry)
        else:
            return 0
    if values:
        return 0
    return 1


if __name__ == '__main__':
    print(solution([4, 1, 3, 2]))  # 1
    print(solution([4, 1, 3]))  # 0
    print(solution([4, 1, 3, 2, 3]))  # 0
    print(solution([4, 1, 3, 3]))  # 0
