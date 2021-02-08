# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/5672682212c8ecf83e000050
#
# Twice linear

import bisect


def sorted_insert(lst, value):
    idx = bisect.bisect_left(lst, value)
    if idx == len(lst):
        lst.append(value)
    elif lst[idx] != value:
        lst.insert(idx, value)


def dbl_linear(n):
    u = [1]
    idx = 0
    while len(u) < n + 1:
        sorted_insert(u, 2 * u[idx] + 1)
        sorted_insert(u, 3 * u[idx] + 1)
        idx += 1

    while 2 * u[idx] + 1 < u[n]:
        sorted_insert(u, 2 * u[idx] + 1)
        sorted_insert(u, 3 * u[idx] + 1)
        idx += 1

    return u[n]


if __name__ == '__main__':
    print(dbl_linear(10))  # 22
    print(dbl_linear(20))  # 57
    print(dbl_linear(30))  # 91
    print(dbl_linear(50))  # 175
