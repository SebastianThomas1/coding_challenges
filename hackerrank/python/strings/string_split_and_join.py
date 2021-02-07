# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/python-string-split-and-join
#
# String Split and Join

def split_and_join(line):
    return '-'.join(line.split(' '))


if __name__ == '__main__':
    print(split_and_join('this is a string'))  # this-is-a-string
