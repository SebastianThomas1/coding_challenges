# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/itertools-combinations
#
# itertools.combinations()

from itertools import combinations


def print_combinations(string, max_size):
    for size in range(1, max_size + 1):
        for s in combinations(sorted(list(string)), size):
            print(''.join(s))


if __name__ == '__main__':
    print_combinations('HACK', 2)
