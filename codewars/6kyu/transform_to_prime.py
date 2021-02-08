# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/5a946d9fba1bb5135100007c
#
# Transform To Prime

def is_divisible_by(a, l):
    return any([not (a % d) for d in l])


def primes_up_to(n):
    primes = []
    for a in range(2, n + 1):
        if not is_divisible_by(a, [prime for prime in primes if
                                   not prime * prime > a]):
            primes.append(a)
    return primes


def minimum_number(numbers):
    sum_numbers = sum(numbers)
    difference = 0
    primes = primes_up_to(int(sum_numbers**(1 / 2)))
    while is_divisible_by(sum_numbers + difference, primes):
        difference += 1
    return difference


if __name__ == '__main__':
    print(minimum_number([3, 1, 2]))  # 1
    print(minimum_number([2, 12, 8, 4, 6]))  # 5
    print(minimum_number([50, 39, 49, 6, 17, 28]))  # 2
