# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/jumping-on-the-clouds
#
# Jumping on the Clouds

def jumping_on_clouds(c):
    idx = 0
    n = len(c)

    count_jumps = 0
    while idx < n - 1:
        if idx + 2 < n:
            if c[idx + 2]:
                idx += 1
            else:
                idx += 2
        else:
            idx += 1
        count_jumps += 1

    return count_jumps


if __name__ == '__main__':
    print(jumping_on_clouds([0, 0, 1, 0, 0, 1, 0]))
    print(jumping_on_clouds([0, 0, 0, 0, 1, 0]))
