# Sebastian Thomas (coding at sebastianthomas dot de)

# https://leetcode.com/problems/interleaving-string/
#
# 97. Interleaving String
#
# Given strings s1, s2, and s3, find whether s3 is formed by an
# interleaving of s1 and s2.
#
# An interleaving of two strings s and t is a configuration where they
# are divided into non-empty substrings such that:
#
# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or
# t1 + s1 + t2 + s2 + t3 + s3 + ...
#
# Note: a + b is the concatenation of strings a and b.

def is_interleave(s1: str, s2: str, s3: str, cache=None) -> bool:
    if cache is None:
        cache = {}
    if not s1:
        return s2 == s3
    if not s2:
        return s1 == s3
    if not s3:
        return False

    if (s1, s2, s3) not in cache:
        cache[(s1, s2, s3)] \
            = (s1[0] == s3[0] and is_interleave(s1[1:], s2, s3[1:], cache)
               or s2[0] == s3[0] and is_interleave(s1, s2[1:], s3[1:], cache))

    return cache[(s1, s2, s3)]


if __name__ == '__main__':
    print(is_interleave('aabcc', 'dbbca', 'aadbbcbcac'))  # True
    print(is_interleave('aabcc', 'dbbca', 'aadbbbaccc'))  # False
    print(is_interleave('', '', ''))  # True
    print(is_interleave('bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbaba'
                        'bbbbbabbbbababbabaabababbbaabababababbbaaababaa',
                        'babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaa'
                        'bbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab',
                        'babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaa'
                        'aaabbbbaabbaaabababbaaaaaabababbababaababbababbbababb'
                        'bbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaab'
                        'bbbbabbbbaabbabaabbbbabaaabbababbabbabbab'))
    # False
