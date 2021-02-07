# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/itertools-permutations
#
# itertools.permutations()

from itertools import permutations


def print_permutations(string, size):
    for s in permutations(sorted(list(string)), size):
        print(''.join(s))


if __name__ == '__main__':
    print_permutations('HACK', 2)
