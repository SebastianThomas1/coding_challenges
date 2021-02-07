# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/dynamic-array
#
# Dynamic Array

def dynamic_array(n, queries):
    arr = []
    for _ in range(n):
        arr.append([])

    last_answer = 0

    res = []
    for query in queries:
        mode, x, y = query
        idx = (x ^ last_answer) % n
        if mode == 1:
            arr[idx].append(y)
        else:
            last_answer = arr[idx][y % len(arr[idx])]
            res.append(last_answer)

    return res


if __name__ == '__main__':
    print(dynamic_array(2, [[1, 0, 5],
                            [1, 1, 7],
                            [1, 0, 3],
                            [2, 1, 0],
                            [2, 1, 1]]))  # [7, 3]
