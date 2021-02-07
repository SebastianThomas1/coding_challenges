# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/repeated-string
#
# Repeated String

def repeated_string(s, n):
    q, r = divmod(n, len(s))
    return q * s.count('a') + s[:r].count('a')


if __name__ == '__main__':
    print(repeated_string('aba', 10))  # 7
    print(repeated_string('a', 1000000000000))  # 1000000000000
