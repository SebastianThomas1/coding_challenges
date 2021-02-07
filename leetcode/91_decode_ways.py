# Sebastian Thomas (coding at sebastianthomas dot de)

# https://leetcode.com/problems/decode-ways/
#
# 91. Decode Ways
#
# A message containing letters from A-Z can be encoded into numbers
# using the following mapping:
#
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
#
# To decode an encoded message, all the digits must be grouped then
# mapped back into letters using the reverse of the mapping above (there
# may be multiple ways). For example, "11106" can be mapped into:
#
# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
#
# Note that the grouping (1 11 06) is invalid because "06" cannot be
# mapped into 'F' since "6" is different from "06".
#
# Given a string s containing only digits, return the number of ways to
# decode it.
#
# The answer is guaranteed to fit in a 32-bit integer.

DOUBLE_DIGITS = {'11', '12', '13', '14', '15', '16', '17', '18', '19', '21',
                 '22', '23', '24', '25', '26'}


def num_decodings(s: str) -> int:
    if s[0] == '0':
        return 0

    last_count = 1
    count = 1
    for idx in range(1, len(s)):
        if s[idx - 1:idx + 1] in DOUBLE_DIGITS \
                and (idx == len(s) - 1 or s[idx + 1] != '0'):
            last_count, count = count, last_count + count
        elif s[idx] != '0' or s[idx - 1] == '1' or s[idx - 1] == '2':
            last_count = count
        else:
            return 0

    return count


if __name__ == '__main__':
    print(num_decodings('12'))  # 2
    print(num_decodings('226'))  # 3
    print(num_decodings('0'))  # 0
    print(num_decodings('1'))  # 1
    print(num_decodings('90'))  # 0
    print(num_decodings('1234321'))  # 6
    print(num_decodings('10'))  # 1
    print(num_decodings('2101'))  # 1
