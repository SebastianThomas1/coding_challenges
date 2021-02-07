# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/the-hurdle-race
#
# The Hurdle Race

def hurdle_race(k, height):
    return max(max(height) - k, 0)


if __name__ == '__main__':
    print(hurdle_race(4, [1, 6, 3, 5, 2]))
    print(hurdle_race(7, [2, 5, 4, 5, 2]))
