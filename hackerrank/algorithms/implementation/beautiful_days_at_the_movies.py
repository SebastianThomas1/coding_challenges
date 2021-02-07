# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies
#
# Beautiful Days at the Movies

def difference_with_reverse(a):
    return abs(a - int(str(a)[::-1]))


def beautiful_days(i, j, k):
    return sum(1 for day in range(i, j + 1)
               if not difference_with_reverse(day) % k)


if __name__ == '__main__':
    print(beautiful_days(20, 23, 6))  # 2
