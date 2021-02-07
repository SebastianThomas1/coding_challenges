# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/python-print
#
# Print Function

def string_numbers(n):
    return ''.join(map(str, range(1, n + 1)))


if __name__ == '__main__':
    print(string_numbers(3))  # 123
