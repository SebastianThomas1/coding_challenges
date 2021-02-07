# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/plus-minus
#
# Plus Minus

def plus_minus(arr):
    n_pos = 0
    n_neg = 0
    for value in arr:
        if value > 0:
            n_pos += 1
        elif value < 0:
            n_neg += 1

    n = len(arr)
    print('{:.6f}'.format(n_pos / n))
    print('{:.6f}'.format(n_neg / n))
    print('{:.6f}'.format((n - n_pos - n_neg) / n))


if __name__ == '__main__':
    plus_minus([-4, 3, -9, 0, 4, 1])
    # 0.500000
    # 0.333333
    # 0.166667
