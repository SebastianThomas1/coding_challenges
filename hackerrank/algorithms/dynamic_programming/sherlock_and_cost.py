# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/sherlock-and-cost
#
# Sherlock and Cost

def cost(b):
    max_sum_ending_low = 0
    max_sum_ending_high = 0
    for idx in range(1, len(b)):
        max_sum_ending_low, max_sum_ending_high \
            = (max(max_sum_ending_low, max_sum_ending_high + b[idx - 1] - 1),
               max(max_sum_ending_high + abs(b[idx] - b[idx - 1]),
                   max_sum_ending_low + b[idx] - 1))

    return max(max_sum_ending_low, max_sum_ending_high)


if __name__ == '__main__':
    print(cost([10, 1, 10, 1, 10]))  # 36
    print(cost([100, 2, 100, 2, 100]))  # 396
    print(cost([3, 15, 4, 12, 10]))  # 50
    print(cost([4, 7, 9]))  # 12
