# Sebastian Thomas (coding at sebastianthomas dot de)

# https://leetcode.com/problems/regular-expression-matching/
#
# 10. Regular Expression Matching
#
# Given an input string (s) and a pattern (p), implement regular
# expression matching with support for '.' and '*' where:
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

def isMatch(s: str, p: str) -> bool:
    # matches[i][j] indicates whether s[i:] matches p[j:]
    matches = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

    matches[-1][-1] = True
    for i in range(len(s), -1, -1):
        for j in range(len(p) - 1, -1, -1):
            if j + 1 < len(p) and p[j + 1] == '*':  # p[j:] == 'x*…'
                matches[i][j] = matches[i][j + 2] \
                                or i < len(s) and p[j] in {s[i], '.'} \
                                and matches[i + 1][j]
                # true if s[i:] and p[j + 2:] == '…' match
                # or if s[i] and p[j] match
                # and s[i + 1:] and p[j:] match
            else:
                matches[i][j] = i < len(s) and p[j] in {s[i], '.'} \
                                and matches[i + 1][j + 1]
                # true if s[i] and p[j] match
                # and s[i + 1:] and p[j + 1:] match

    return matches[0][0]


if __name__ == '__main__':
    print(isMatch('aa', 'a'))  # False
    print(isMatch('aa', 'a*'))  # True
    print(isMatch('ab', '.*'))  # True
    print(isMatch('aab', 'c*a*b'))  # True
    print(isMatch('mississippi', 'mis*is*p*.'))  # False
    print(isMatch('ab', 'ab'))  # True
    print(isMatch('ab', 'a.'))  # True
    print(isMatch('ab', '.b'))  # True
    print(isMatch('ab', '..'))  # True
