# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/5a045fee46d843effa000070
#
# Factorial decomposition

from collections import defaultdict


def primes_up_to(n):
    primes = []
    for a in range(2, n + 1):
        if not any([not(a % prime) for prime in primes if not prime*prime > a]):
            primes.append(a)
    return primes


def decomp(n):
    primes = primes_up_to(n)
    exponents = defaultdict(int)
    for a in range(1, n + 1):
        b = a
        for prime in primes:
            while not(b % prime):
                b /= prime
                exponents[prime] += 1
    return ' * '.join([f'{prime}^{exponents[prime]}' if exponents[prime] != 1
                       else str(prime) for prime in primes])


if __name__ == '__main__':
    print(decomp(12))  # 2^10 * 3^5 * 5^2 * 7 * 11
    print(decomp(22))  # 2^19 * 3^9 * 5^4 * 7^3 * 11^2 * 13 * 17 * 19
    print(decomp(25))  # 2^22 * 3^10 * 5^6 * 7^3 * 11^2 * 13 * 17 * 19 * 23
