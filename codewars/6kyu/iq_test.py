# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/552c028c030765286c00007d
#
# IQ test

def iq_test(numbers):
    even_indices = []
    odd_indices = []
    for idx, number in enumerate(map(int, numbers.split())):
        if number % 2 == 0:
            even_indices.append(idx)
        else:
            odd_indices.append(idx)

    return (even_indices[0] if len(even_indices) == 1 else odd_indices[0]) + 1


if __name__ == '__main__':
    print(iq_test('2 4 7 8 10'))  # 3
    print(iq_test('1 2 1 1'))  # 2
    print(iq_test('1 2 2'))  # 1
