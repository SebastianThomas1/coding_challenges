# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/the-birthday-bar
#
# Subarray Division

def birthday(s, d, m):
    return sum(1 for idx in range(len(s) - m + 1) if sum(s[idx:idx + m]) == d)


if __name__ == '__main__':
    print(birthday([1, 2, 1, 3, 2], 3, 2))  # 2
    print(birthday([1, 1, 1, 1, 1, 1], 3, 2))  # 0
    print(birthday([4], 4, 1))  # 1
