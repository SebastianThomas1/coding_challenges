# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/compress-the-string
#
# Compress the String!

from itertools import groupby


def compress_string(s):
    return ' '.join('({}, {})'.format(len(list(grouper)), key)
                    for key, grouper in groupby(s))


if __name__ == '__main__':
    print(compress_string('1222311'))
