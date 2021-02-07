# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/swap-case
#
# sWAP cASE

def swap_case(s):
    swapped_chars = []
    for char in s:
        if char.islower():
            swapped_chars.append(char.upper())
        elif char.isupper():
            swapped_chars.append(char.lower())
        else:
            swapped_chars.append(char)

    return ''.join(swapped_chars)


if __name__ == '__main__':
    print(swap_case('HackerRank.com presents "Pythonist 2".'))
    # hACKERrANK.COM PRESENTS "pYTHONIST 2".
