# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/5886e082a836a691340000c3
#
# Simple Fun #27: Rectangle Rotation

import math


def rectangle_rotation(a, b):
    if b > a:
        a, b = b, a

    c = b/(2*math.sqrt(2))
    d = a/(2*math.sqrt(2))

    k = int(2*c)
    l = int(2*d)
    m = int(d - c)
    n = k + l - 2*m - 1

    if n % 2 == 1:
        return (2*k + 1) * (2*m + 1) + int((n + 1)**2/2)
    else:
        return (2*k + 1) * (2*m + 1) + 2*k*(k + 1)


if __name__ == '__main__':
    print(rectangle_rotation(6, 4))  # 23
    print(rectangle_rotation(30, 2))  # 65
    print(rectangle_rotation(8, 6))  # 49
    print(rectangle_rotation(16, 20))  # 333
