# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/sherlock-and-anagrams
#
# Sherlock and Anagrams

from collections import defaultdict


def sherlock_and_anagrams(s):
    length = len(s)

    # construct counter for sorted substrings
    counter = defaultdict(int)
    for i in range(length):
        for j in range(i + 1, length + 1):
            counter[''.join(sorted(s[i:j]))] += 1

    return sum(counter[normalized] * (counter[normalized] - 1) // 2
               for normalized in counter)


if __name__ == '__main__':
    print(sherlock_and_anagrams('mom'))  # 2
    print(sherlock_and_anagrams('abba'))  # 4
    print(sherlock_and_anagrams('abcd'))  # 0
    print(sherlock_and_anagrams('ifailuhkqq'))  # 3
    print(sherlock_and_anagrams('kkkk'))  # 10
    print(sherlock_and_anagrams('cdcd'))  # 5
