# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/53e57dada0cb0400ba000688
#
# Alphabetic Anagrams

from collections import Counter
from copy import copy


def multinomial(lst):
    """Computes the multinomial coefficient of sum(lst) over lst."""
    res = 1
    cur_numerator = sum(lst)
    idx_max = max(range(len(lst)), key=lst.__getitem__)
    # factorial(max(lst)) occurs in the numerator as well as in the
    # denominator, so it can be shortened
    for value in lst[:idx_max] + lst[idx_max + 1:]:
        for cur_denominator in range(1, value + 1):
            res *= cur_numerator
            res //= cur_denominator
            cur_numerator -= 1
    return res


def list_position(word):
    if len(word) == 1:
        return 1
    else:
        chars = sorted(set(word))
        frequencies = Counter(word)
        lead_char_idx = chars.index(word[0])

        # compute the count of words starting with a character that
        # occurs before the given lead character word[0]
        count = 0
        for idx, char in enumerate(chars[:lead_char_idx]):
            reduced_frequencies = copy(frequencies)
            reduced_frequencies[char] -= 1
            count += multinomial(list(reduced_frequencies.values()))

        return count + list_position(word[1:])


if __name__ == '__main__':
    print(list_position('ABAB'))  # 2
    print(list_position('AAAB'))  # 1
    print(list_position('BAAA'))  # 4
    print(list_position('QUESTION'))  # 24572
    print(list_position('BOOKKEEPER'))  # 10743
