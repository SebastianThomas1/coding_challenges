# Sebastian Thomas (coding at sebastianthomas dot de)

# https://leetcode.com/problems/word-break-ii/
#
# 140. Word Break II
#
# Given a non-empty string s and a dictionary wordDict containing a list
# of non-empty words, add spaces in s to construct a sentence where each
# word is a valid dictionary word. Return all such possible sentences.
#
# Note:
#
# The same word in the dictionary may be reused multiple times in the
# segmentation.
# You may assume the dictionary does not contain duplicate words.

from typing import List


def word_break(s: str, word_dict: List[str], memo=None) -> List[str]:
    if memo is None:
        memo = {}
    if s == '':
        return ['']

    if s not in memo:
        memo[s] = []
        for word in word_dict:
            try:
                idx = s.index(word)
            except ValueError:
                continue
            else:
                if idx == 0:
                    memo[s].extend(' '.join([word] + partition.split())
                                   for partition in word_break(
                        s[len(word):], word_dict, memo))

    return memo[s]


if __name__ == '__main__':
    print(word_break('catsanddog', ['cat', 'cats', 'and', 'sand', 'dog']))
    # ['cats and dog', 'cat sand dog']
    print(word_break('pineapplepenapple',
                     ['apple', 'pen', 'applepen', 'pine', 'pineapple']))
    # ['pine apple pen apple', 'pineapple pen apple', 'pine applepen apple']
    print(word_break('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']))
    # []
