# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement
#
# itertools.combinations_with_replacement()

from itertools import combinations_with_replacement


def print_combinations_with_replacement(string, size):
    for s in combinations_with_replacement(sorted(list(string)), size):
        print(''.join(s))


if __name__ == '__main__':
    print_combinations_with_replacement('HACK', 2)
