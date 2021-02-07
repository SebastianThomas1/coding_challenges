# Sebastian Thomas (coding at sebastianthomas dot de)

# https://leetcode.com/problems/wildcard-matching/
#
# 44. Wildcard Matching
#
# Given an input string (s) and a pattern (p), implement wildcard
# pattern matching with support for '?' and '*' where:
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

def is_match(s: str, p: str) -> bool:
    # matches[i][j] indicates whether s[i:] matches p[j:]
    matches = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

    matches[-1][-1] = True
    for i in range(len(s), -1, -1):
        for j in range(len(p) - 1, -1, -1):
            if p[j] == '*':  # p[j:] == '*…'
                matches[i][j] = matches[i][j + 1] or i < len(s) \
                                and (matches[i + 1][j]
                                     or matches[i + 1][j + 1])
                # true if s[i:] and p[j + 1:] == '…' match
                # (* stands for no characters)
                # or if s[i + 1:] and p[j:] match
                # (* stands for multiple characters)
                # and s[i + 1:] and p[j + 1:] match
                # (* stands for precisely one character)
            else:
                matches[i][j] = i < len(s) and p[j] in {s[i], '?'} \
                                and matches[i + 1][j + 1]
                # true if s[i] and p[j] match
                # and s[i + 1:] and p[j + 1:] match

    return matches[0][0]


if __name__ == '__main__':
    print(is_match('aa', 'a'))  # False
    print(is_match('aa', '*'))  # True
    print(is_match('cb', '?a'))  # False
    print(is_match('adceb', '*a*b'))  # True
    print(is_match('acdcb', 'a*c?b'))  # False
