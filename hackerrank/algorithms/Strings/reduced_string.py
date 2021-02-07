# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/reduced-string
#
# Super Reduced String

def super_reduced_string(s):
    if not s:
        return 'Empty String'

    for idx in range(len(s) - 1):
        if s[idx] == s[idx + 1]:
            return super_reduced_string(s[:idx] + s[idx + 2:])

    return s


if __name__ == '__main__':
    print(super_reduced_string('aaabccddd'))  # abd
    print(super_reduced_string('aa'))  # Empty String
    print(super_reduced_string('baab'))  # Empty String
