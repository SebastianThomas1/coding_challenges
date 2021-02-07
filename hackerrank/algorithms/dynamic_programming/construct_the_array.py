# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/construct-the-array
#
# Construct the Array

def count_array(n, k, x):
    count_ending_with_1 = 1
    count_ending_with_2 = 0
    # in each step, we have count_ending_with_x == count_ending_with_2
    # for each x != 1; so it suffices to compute count_ending_with_2

    for _ in range(2, n + 1):
        count_ending_with_1, count_ending_with_2 \
            = (count_ending_with_2 * (k - 1),
               count_ending_with_1 + count_ending_with_2 * (k - 2))
        count_ending_with_1 %= 10**9 + 7
        count_ending_with_2 %= 10**9 + 7

    return count_ending_with_1 if x == 1 else count_ending_with_2


if __name__ == '__main__':
    print(count_array(4, 3, 2))  # 3
