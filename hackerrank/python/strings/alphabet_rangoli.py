# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/alphabet-rangoli
#
# Alphabet Rangoli

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def print_rangoli(size):
    for idx in range(size):
        inner_char_idx = size - 1 - idx
        chars = list(ALPHABET[inner_char_idx:size])
        print('-'*2*inner_char_idx + '-'.join(chars[::-1] + chars[1:])
              + '-'*2*inner_char_idx)
    for idx in range(size - 2, -1, -1):
        inner_char_idx = size - 1 - idx
        chars = list(ALPHABET[inner_char_idx:size])
        print('-'*2*inner_char_idx + '-'.join(chars[::-1] + chars[1:])
              + '-'*2*inner_char_idx)


if __name__ == '__main__':
    print_rangoli(5)
    # --------e--------
    # ------e-d-e------
    # ----e-d-c-d-e----
    # --e-d-c-b-c-d-e--
    # e-d-c-b-a-b-c-d-e
    # --e-d-c-b-c-d-e--
    # ----e-d-c-d-e----
    # ------e-d-e------
    # --------e--------
