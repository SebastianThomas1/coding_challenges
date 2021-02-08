# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/5b7176768adeae9bc9000056
#
# Element equals its index

def index_equals_value(arr):
    if not arr:
        return -1

    left = 0
    mid = 0
    right = len(arr) - 1

    while left <= right:
        # mid = left + (right - left) // 2
        mid = left + (right - left) // 2

        if arr[mid] == mid:
            if left == right:
                return mid
            else:
                right = mid
        elif arr[mid] > mid:
            right = mid - 1
        else:
            left = mid + 1

    return mid if arr[mid] == mid else -1


if __name__ == '__main__':
    print(index_equals_value([-8, 0, 2, 5]))  # 2
    print(index_equals_value([-1, 0, 3, 6]))  # -1
    print(index_equals_value([-3, 0, 1, 3, 10]))  # 3
    print(index_equals_value([-5, 1, 2, 3, 4, 5, 7, 10, 15]))  # 1
    print(index_equals_value([9, 10, 11, 12, 13, 14]))  # -1
    print(index_equals_value([0]))  # 0
    print(index_equals_value([]))  # -1
