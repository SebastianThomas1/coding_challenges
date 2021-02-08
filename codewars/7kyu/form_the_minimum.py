# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/5ac6932b2f317b96980000ca
#
# Form The Minimum

def min_value(digits):
    return int(''.join([str(digit) for digit in sorted(list(set(digits)))]))


if __name__ == '__main__':
    print(min_value([1, 3, 1]))  # 13
    print(min_value([4, 7, 5, 7]))  # 457
    print(min_value([4, 8, 1, 4]))  # 148
    print(min_value([5, 7, 5, 9, 7]))  # 579
    print(min_value([1, 9, 3, 1, 7, 4, 6, 6, 7]))  # 134679
