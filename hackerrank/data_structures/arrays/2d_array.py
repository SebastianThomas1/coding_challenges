# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/2d-array
#
# 2D Array - DS

def hourglass_sum(arr):
    max_h_sum = None
    for k in range(1, 5):
        for l in range(1, 5):
            h_sum = arr[k][l]
            for j in range(l - 1, l + 2):
                h_sum += arr[k - 1][j]
                h_sum += arr[k + 1][j]
            max_h_sum = max(max_h_sum or h_sum, h_sum)

    return max_h_sum


if __name__ == '__main__':
    print(hourglass_sum([[1, 1, 1, 0, 0, 0],
                         [0, 1, 0, 0, 0, 0],
                         [1, 1, 1, 0, 0, 0],
                         [0, 0, 2, 4, 4, 0],
                         [0, 0, 0, 2, 0, 0],
                         [0, 0, 1, 2, 4, 0]]))  # 19
