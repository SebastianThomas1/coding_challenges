# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/5af15a37de4c7f223e00012d
#
# Sort Out The Men From Boys

import bisect


def sorted_insert(lst, value):
    idx = bisect.bisect_left(lst, value)
    if idx == len(lst):
        lst.append(value)
    elif lst[idx] != value:
        lst.insert(idx, value)


def men_from_boys(lst):
    evens = []
    odds = []

    for entry in lst:
        if entry % 2 == 0:
            sorted_insert(evens, entry)
        else:
            sorted_insert(odds, entry)

    return evens + odds[::-1]


if __name__ == '__main__':
    print(men_from_boys([7, 3, 14, 17]))  # [14, 17, 7, 3]
    print(men_from_boys([-94, -99, -100, -99, -96, -99]))
    # [-100, -96, -94, -99]
    print(men_from_boys([49, 818, -282, 900, 928, 281, -282, -1]))
    # [-282, 818, 900, 928, 281, 49, -1]
