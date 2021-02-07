# Sebastian Thomas (coding at sebastianthomas dot de)

# https://leetcode.com/problems/distinct-subsequences/
#
# 115. Distinct Subsequences
#
# Given two strings s and t, return the number of distinct subsequences
# of s which equals t.
#
# A string's subsequence is a new string formed from the original string
# by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (i.e., "ACE" is a
# subsequence of "ABCDE" while "AEC" is not).
#
# It's guaranteed the answer fits on a 32-bit signed integer.

def num_distinct(s: str, t: str) -> int:
    m = len(s)
    n = len(t)

    # possibilities in i-th iteration:
    # idx j: number of possibilities of t[:j] occurs in s[:i]
    possibilities = [0] * (n + 1)
    possibilities[0] = 1
    for i in range(1, m + 1):
        for j in range(min(i + 1, n), 0, -1):
            if s[i - 1] == t[j - 1]:
                possibilities[j] += possibilities[j - 1]

    return possibilities[-1]


if __name__ == '__main__':
    print(num_distinct('rabbbit', 'rabbit'))  # 3
    print(num_distinct('babgbag', 'bag'))  # 5
