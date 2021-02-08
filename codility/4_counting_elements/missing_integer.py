# Sebastian Thomas (coding at sebastianthomas dot de)

# https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/
#
# MissingInteger
#
# Find the smallest positive integer that does not occur in a given
# sequence.
#
# This is a demo task.
#
# Write a function:
#   def solution(A)
# that, given an array A of N integers, returns the smallest positive
# integer (greater than 0) that does not occur in A.
#
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return
# 5.
#
# Given A = [1, 2, 3], the function should return 4.
#
# Given A = [−1, −3], the function should return 1.
#
# Write an efficient algorithm for the following assumptions:
#   - N is an integer within the range [1..100,000];
#   - each element of array A is an integer within the range
#     [−1,000,000..1,000,000].

def solution(a):
    value = 1
    for entry in sorted(a):
        if value == entry:
            value += 1
        elif value < entry:
            break

    return value


if __name__ == '__main__':
    print(solution([1, 3, 6, 4, 1, 2]))  # 5
    print(solution([1, 2, 3]))  # 4
    print(solution([-1, -3]))  # 1
    print(solution([3, 2, 1]))  # 4
