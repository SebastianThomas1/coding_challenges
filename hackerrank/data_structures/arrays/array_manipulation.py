# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/crush
#
# Array Manipulation

def array_manipulation(n, queries):
    a = [0] * n
    for query in queries:
        i, j, value = query
        a[i - 1] += value
        if j < n:
            a[j] -= value

    value = 0
    max_value = None
    for idx in range(n):
        value += a[idx]
        if max_value is None or value > max_value:
            max_value = value

    return max_value


if __name__ == '__main__':
    print(array_manipulation(10, [[1, 5, 3], [4, 8, 7], [6, 9, 1]]))
    print(array_manipulation(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]]))
