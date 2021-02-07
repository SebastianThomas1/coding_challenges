# Sebastian Thomas (coding at sebastianthomas dot de)

# https://leetcode.com/problems/longest-substring-without-repeating-characters/
#
# 3. Longest Substring Without Repeating Characters
#
# Given a string s, find the length of the longest substring without
# repeating characters.

def length_of_longest_substring(s: str) -> int:
    max_length = 0
    index_of_char = {}

    start_idx = 0
    for idx, char in enumerate(s):
        if char in index_of_char and start_idx <= index_of_char[char]:
            start_idx = index_of_char[char] + 1

        index_of_char[char] = idx

        max_length = max(max_length, idx - start_idx + 1)

    return max_length


if __name__ == '__main__':
    print(length_of_longest_substring('abcabcbb'))  # 3
    print(length_of_longest_substring('bbbbb'))  # 1
    print(length_of_longest_substring('pwwkew'))  # 3
    print(length_of_longest_substring(''))  # 0
