# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/text-wrap
#
# Text Wrap

def wrap(string, max_width):
    return '\n'.join([string[idx*max_width:(idx + 1)*max_width]
                      for idx in range(len(string) // max_width + 1)])


if __name__ == '__main__':
    print(wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4))
    # ABCD
    # EFGH
    # IJKL
    # IMNO
    # QRST
    # UVWX
    # YZ
