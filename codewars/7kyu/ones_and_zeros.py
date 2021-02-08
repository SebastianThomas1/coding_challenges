# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/578553c3a1b8d5c40300037c
#
# Ones and Zeros

def binary_array_to_number(binary):
    n = len(binary)

    return sum([binary[k] * 2**(n - k - 1) for k in range(n)])


if __name__ == '__main__':
    print(binary_array_to_number([0, 0, 0, 1]))  # 1
    print(binary_array_to_number([0, 0, 1, 0]))  # 2
    print(binary_array_to_number([1, 1, 1, 1]))  # 15
    print(binary_array_to_number([0, 1, 1, 0]))  # 6
