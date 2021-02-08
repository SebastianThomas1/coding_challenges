# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/585d7d5adb20cf33cb000235
#
# Find the unique number

def find_uniq(numbers):
    first_number = numbers[0]
    if first_number not in numbers[1:]:
        return first_number
    else:
        unique_numbers = set(numbers)
        unique_numbers.remove(first_number)
        return next(iter(unique_numbers))


if __name__ == '__main__':
    print(find_uniq([1, 1, 1, 2, 1, 1]))  # 2
    print(find_uniq([0, 0, 0.55, 0, 0]))  # 0.55
    print(find_uniq([3, 10, 3, 3, 3]))  # 10
