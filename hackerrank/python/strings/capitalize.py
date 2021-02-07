# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/capitalize
#
# Capitalize!

def solve(s):
    return ' '.join(substring.capitalize() for substring in s.split(' '))


if __name__ == '__main__':
    print(solve('chris alan'))  # Chris Alan
