# Sebastian Thomas (coding at sebastianthomas dot de)

# https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/
#
# CountDiv
#
# Compute number of integers divisible by k in range [a..b].
#
# Write a function:
#   def solution(A, B, K)
# that, given three integers A, B and K, returns the number of integers
# within the range [A..B] that are divisible by K, i.e.:
#   { i : A ≤ i ≤ B, i mod K = 0 }
# For example, for A = 6, B = 11 and K = 2, your function should return
# 3, because there are three numbers divisible by 2 within the range
# [6..11], namely 6, 8 and 10.
#
# Write an efficient algorithm for the following assumptions:
#   - A and B are integers within the range [0..2,000,000,000];
#   - K is an integer within the range [1..2,000,000,000];
#   - A ≤ B.

def count_of_divisible_integers_up_to(a, k):
    return a // k + 1


def solution(a, b, k):
    return (count_of_divisible_integers_up_to(b, k)
            - count_of_divisible_integers_up_to(a - 1, k))


if __name__ == '__main__':
    print(solution(6, 11, 2))  # 3
    print(solution(7, 11, 2))  # 2
    print(solution(6, 12, 2))  # 4
    print(solution(7, 12, 2))  # 3
    print(solution(6, 6, 2))  # 1
    print(solution(7, 7, 2))  # 0
    print(solution(6, 11, 3))  # 2
    print(solution(7, 11, 3))  # 1
    print(solution(6, 12, 3))  # 3
    print(solution(7, 12, 3))  # 2
    print(solution(6, 6, 3))  # 1
    print(solution(7, 7, 3))  # 0
