# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/two-strings
#
# Two Strings

def two_strings(s1, s2):
    chars1 = set(s1)
    chars2 = set(s2)
    return 'NO' if chars1.isdisjoint(chars2) else 'YES'


if __name__ == '__main__':
    print(two_strings('hello', 'world'))  # YES
    print(two_strings('hi', 'world'))  # NO
