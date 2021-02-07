# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/apple-and-orange
#
# Apple and Orange

def count_apples_and_oranges(s, t, a, b, apples, oranges):
    count = 0
    for diff in apples:
        position = a + diff
        if position >= s and position <= t:
            count += 1
    print(count)

    count = 0
    for diff in oranges:
        position = b + diff
        if position >= s and position <= t:
            count += 1
    print(count)


if __name__ == '__main__':
    count_apples_and_oranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])
    # 1
    # 1
