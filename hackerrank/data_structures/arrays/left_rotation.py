# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/array-left-rotation
#
# Left rotation

def rotate_left(d, arr):
    for _ in range(d):
        arr.append(arr.pop(0))
    return arr


if __name__ == '__main__':
    print(rotate_left(4, [1, 2, 3, 4, 5]))  # [5, 1, 2, 3, 4]
