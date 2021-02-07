# 5. Longest Palindromic Substring
#
# Given a string s, return the longest palindromic substring in s.

def longest_palindrome(s: str) -> str:
    if s == '':
        return ''

    # compute list of palindrome end indices (index is start index)
    palindromes = [0]
    for end_idx in range(1, len(s)):
        for idx in range(1, end_idx):
            if palindromes[idx] == end_idx - 1 and s[idx - 1] == s[end_idx]:
                palindromes[idx - 1] = end_idx

        if s[end_idx - 1] == s[end_idx]:
            palindromes[end_idx - 1] = end_idx

        palindromes.append(end_idx)

    # determine index with palindrome of maximal length
    max_idx = None
    max_length = 0
    idx = 0
    while idx < len(s):
        length = palindromes[idx] - idx + 1
        if length > max_length:
            max_length = length
            max_idx = idx
        idx += 1

    # return palindrome
    return s[max_idx:palindromes[max_idx] + 1]


if __name__ == '__main__':
    print(longest_palindrome('babad'))  # bab
    print(longest_palindrome('cbbd'))  # bb
    print(longest_palindrome('a'))  # a
    print(longest_palindrome('ac'))  # a
    print(longest_palindrome('abacab'))  # bacab
