# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/diagonal-difference
#
# Diagonal Difference

def diagonal_difference(arr):
    n = len(arr)
    return abs(sum(arr[idx][idx] for idx in range(n))
               - sum(arr[idx][n - idx - 1] for idx in range(n)))


if __name__ == '__main__':
    print(diagonal_difference([[11, 2, 4],
                               [4, 5, 6],
                               [10, 8, -12]]))  # 15
