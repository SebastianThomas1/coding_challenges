# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/kangaroo
#
# Number Line Jumps

def kangaroo(x1, v1, x2, v2):
    return 'NO' if v1 == v2 and x1 != x2 or (x2 - x1) % (v1 - v2) \
                   or (x2 - x1) / (v1 - v2) < 0 else 'YES'


if __name__ == '__main__':
    print(kangaroo(0, 3, 4, 2))  # YES
    print(kangaroo(0, 2, 5, 3))  # NO
