# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/5552101f47fc5178b1000050
#
# Playing with digits

def dig_pow(n, p):
    sum_of_powers = sum(int(digit_char)**(p + idx)
                        for idx, digit_char in enumerate(str(n)))

    q, r = divmod(sum_of_powers, n)

    return q if r == 0 else -1


if __name__ == '__main__':
    print(dig_pow(89, 1))  # 1
    print(dig_pow(92, 1))  # -1
    print(dig_pow(695, 2))  # 2
    print(dig_pow(46288, 3))  # 51
