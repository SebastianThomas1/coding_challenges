# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/minimum-swaps-2
#
# Minimum Swaps 2

def minimum_swaps(arr):
    index = {value: idx for idx, value in enumerate(arr)}
    count = 0
    for idx in range(len(arr)):
        if arr[idx] != idx + 1:
            change_idx = index[idx + 1]
            index[arr[idx]] = index[idx + 1]
            arr[change_idx] = arr[idx]
            # we do not need arr[idx] == arr[change_idx]
            count += 1

    return count


if __name__ == '__main__':
    print(minimum_swaps([4, 3, 1, 2]))  # 3
    print(minimum_swaps([2, 3, 4, 1, 5]))  # 3
    print(minimum_swaps([1, 3, 5, 2, 4, 6, 7]))  # 3
