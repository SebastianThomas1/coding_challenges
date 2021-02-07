# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/equal-stacks
#
# Equal Stacks

def equal_stacks(h1, h2, h3):
    sum1 = sum(h1)
    sum2 = sum(h2)
    sum3 = sum(h3)

    while True:
        if sum1 == sum2 and sum2 == sum3:
            return sum1
        else:
            max_sum = max(sum1, sum2, sum3)
            if sum1 == max_sum:
                sum1 -= h1.pop(0)
            elif sum2 == max_sum:
                sum2 -= h2.pop(0)
            elif sum3 == max_sum:
                sum3 -= h3.pop(0)


if __name__ == '__main__':
    print(equal_stacks([3, 2, 1, 1, 1], [4, 3, 2], [1, 1, 4, 1]))  # 5
