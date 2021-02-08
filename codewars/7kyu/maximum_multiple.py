# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/5aba780a6a176b029800041c
#
# Maximum Multiple

def max_multiple(divisor, bound):
    return (bound // divisor) * divisor


if __name__ == '__main__':
    print(max_multiple(2, 7))  # 6
    print(max_multiple(3, 10))  # 9
    print(max_multiple(7, 17))  # 14
    print(max_multiple(10, 50))  # 50
    print(max_multiple(37, 200))  # 185
    print(max_multiple(7, 100))  # 98
