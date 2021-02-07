# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/itertools-product
#
# itertools.product()

from itertools import product


def product_string(a, b):
    return ' '.join('({}, {})'.format(x, y) for (x, y) in product(a, b))


if __name__ == '__main__':
    print(product_string([1, 2], [3, 4]))
