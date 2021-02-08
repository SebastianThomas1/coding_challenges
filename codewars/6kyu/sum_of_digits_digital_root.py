# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/541c8630095125aba6000c00
#
# Sum of Digits / Digital Root

def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int, str(n))))


if __name__ == '__main__':
    print(digital_root(16))  # 7
    print(digital_root(456))  # 6
