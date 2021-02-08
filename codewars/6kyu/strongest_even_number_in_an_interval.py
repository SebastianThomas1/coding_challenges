# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/5d16af632cf48200254a6244
#
# Strongest even number in an interval

def compute_strength(k):
    v = 0

    while k % 2 == 0:
        k = k / 2
        v += 1

    return v


def strongest_even(n, m):
    strength = 0
    k = n

    strongest = 0
    while k <= m:
        new_strength = compute_strength(k)
        if new_strength > strength:
            strongest = k
            strength = new_strength
        k += 2**strength

    return strongest


if __name__ == '__main__':
    print(strongest_even(1, 2))  # 2
    print(strongest_even(5, 10))  # 8
    print(strongest_even(48, 56))  # 48
    print(strongest_even(129, 193))  # 192
