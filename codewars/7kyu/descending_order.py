# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/5467e4d82edf8bbf40000155
#
# Descending Order

def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))


if __name__ == '__main__':
    print(descending_order(42145))  # 54421
    print(descending_order(145263))  # 654321
    print(descending_order(123456789))  # 987654321
