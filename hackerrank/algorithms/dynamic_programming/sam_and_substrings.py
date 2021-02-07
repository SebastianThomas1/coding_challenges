# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/sam-and-substrings
#
# Sam and substrings

def substrings(n):
    # substrings = substrings(1234)
    # = substrings(123) + (4 + 34 + 234 + 1234)
    # = substrings(123) + (3 + 23 + 123)*10 + 4*4
    # = substrings(123) + (substrings(123) - substrings(12))*10 + 4*4
    # = substrings(123)*11 - substrings(12)*10 + 4*4
    last_substring_sum = 0
    substring_sum = 0
    for idx in range(len(n)):
        last_substring_sum, substring_sum \
            = (substring_sum,
               substring_sum * 11 - last_substring_sum * 10
               + int(n[idx]) * (idx + 1))
        substring_sum %= 10**9 + 7

    return substring_sum


if __name__ == '__main__':
    print(substrings('16'))  # 23
    print(substrings('123'))  # 164
    print(substrings('1234'))  # 1670
