# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/sock-merchant
#
# Sales by Match

from collections import Counter


def sock_merchant(ar):
    return sum(count // 2 for count in Counter(ar).values())


if __name__ == '__main__':
    print(sock_merchant([1, 2, 1, 2, 1, 3, 2]))  # 2
    print(sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]))  # 3
