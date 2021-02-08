# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/5511b2f550906349a70004e1
#
# Last digit of a large number

def last_digit(a, b):
    return pow(a, b, 10)


if __name__ == '__main__':
    print(last_digit(4, 1))  # 4
    print(last_digit(4, 2))  # 6
    print(last_digit(9, 7))  # 9
    print(last_digit(10, 10**10))  # 0
    print(last_digit(2**200, 2**300))  # 6
