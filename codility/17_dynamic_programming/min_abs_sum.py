# Sebastian Thomas (coding at sebastianthomas dot de)

# https://app.codility.com/programmers/lessons/17-dynamic_programming/min_abs_sum/
#
# MinAbsSum
#
# Given array of integers, find the lowest absolute sum of elements.
#
# For a given array A of N integers and a sequence S of N integers from
# the set {−1, 1}, we define val(A, S) as follows:
#   val(A, S) = |sum {A[i]*S[i] for i = 0..N−1}|
# (Assume that the sum of zero elements equals zero.)
#
# For a given array A, we are looking for such a sequence S that
# minimizes val(A,S).
#
# Write a function:
#   def solution(A)
# that, given an array A of N integers, computes the minimum value of
# val(A, S) from all possible values of val(A, S) for all possible
# sequences S of N integers from the set {−1, 1}.
#
# For example, given array:
#   A[0] =  1
#   A[1] =  5
#   A[2] =  2
#   A[3] = -2
# your function should return 0, since for S = [−1, 1, −1, 1],
# val(A, S) = 0, which is the minimum possible value.
#
# Write an efficient algorithm for the following assumptions:
#   - N is an integer within the range [0..20,000];
#   - each element of array A is an integer within the range
#     [−100..100].

def solution(a):
    # convert A into absolute values, determine largest absolute value,
    # determine sum over all absolute values
    max_abs_value = 0
    sum_abs_values = 0
    for idx, value in enumerate(a):
        if value < 0:
            value = - value
            a[idx] = value
        max_abs_value = max(max_abs_value, value)
        sum_abs_values += value

    # determine counts of absolute values in A
    # do not use Counter, this is a space efficient variant
    # since range of absolute values of A is small ([0, 100])
    count = [0] * (max_abs_value + 1)
    for abs_value in a:
        count[abs_value] += 1

    # determine subsums of absolute values in A by processing every
    # unique absolute value in A at once
    # entry -1 at index means that index is not subsum
    # concrete positive entry is only of importance in an iteration step
    # it gives the remaining count of the absolute value in A that may
    # be added to obtain the next subsum
    is_subsum = [-1] * (sum_abs_values + 1)
    is_subsum[0] = 0
    for abs_value in range(1, max_abs_value + 1):
        if count[abs_value] > 0:
            for i in range(sum_abs_values + 1):
                if is_subsum[i] >= 0:
                    is_subsum[i] = count[abs_value]
                elif i >= abs_value and is_subsum[i - abs_value] > 0:
                    is_subsum[i] = is_subsum[i - abs_value] - 1

    # determine the largest subsum less or equal than half of the sum
    # over all absolute values
    # then sum over all absolute values - 2 * largest subsum is the
    # smallest absolute sum of values in A
    for i in range(sum_abs_values // 2, -1, -1):
        if is_subsum[i] >= 0:
            return sum_abs_values - 2 * i


if __name__ == '__main__':
    print(solution([1, 5, 2, -2]))  # 0
    print(solution([3, 1]))  # 2
