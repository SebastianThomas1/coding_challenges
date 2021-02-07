# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/sparse-arrays
#
# Sparse Arrays

from collections import Counter


def matching_strings(strings, queries):
    counter = Counter(strings)
    return [counter[query] for query in queries]


if __name__ == '__main__':
    print(matching_strings(['aba', 'baba', 'aba', 'xzxb'],
                           ['aba', 'xzxb', 'ab']))
    print(matching_strings(['def', 'de', 'fgh'], ['de', 'lmn', 'fgh']))
    print(matching_strings(['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn',
                            'sdaklfj', 'asdjf', 'na', 'asdjf', 'na', 'basdn',
                            'sdaklfj', 'asdjf'],
                           ['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn']))
