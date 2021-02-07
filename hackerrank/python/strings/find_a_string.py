# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/find-a-string
#
# Find a string

def count_substring(string, sub_string):
    count = 0
    m = len(sub_string)
    for idx in range(len(string) - m + 1):
        if string[idx:idx + m] == sub_string:
            count += 1

    return count


if __name__ == '__main__':
    print(count_substring('ABCDCDC', 'CDC'))  # 2
