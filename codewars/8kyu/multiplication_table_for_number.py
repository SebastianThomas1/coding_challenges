# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce
#
# Multiplication table for number

def multi_table(number):
    return '\n'.join([f'{factor} * {number} = {factor*number}'
                      for factor in range(1, 11)])


if __name__ == '__main__':
    print(multi_table(5))
    # 1 * 5 = 5
    # 2 * 5 = 10
    # 3 * 5 = 15
    # 4 * 5 = 20
    # 5 * 5 = 25
    # 6 * 5 = 30
    # 7 * 5 = 35
    # 8 * 5 = 40
    # 9 * 5 = 45
    # 10 * 5 = 50
    print(multi_table(1))
    # 1 * 1 = 1
    # 2 * 1 = 2
    # 3 * 1 = 3
    # 4 * 1 = 4
    # 5 * 1 = 5
    # 6 * 1 = 6
    # 7 * 1 = 7
    # 8 * 1 = 8
    # 9 * 1 = 9
    # 10 * 1 = 10
