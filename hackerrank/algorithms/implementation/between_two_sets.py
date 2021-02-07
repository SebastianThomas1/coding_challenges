# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/between-two-sets
#
# Between Two Sets

from math import gcd


def primes(n):
    """Returns the primes up to n."""
    sieve = [1] * (n + 1)
    sieve[0] = sieve[1] = 0

    k = 2
    while k * k <= n:
        if sieve[k] == 1:
            for l in range(2 * k, n + 1, k):
                sieve[l] = 0
        k += 1

    res = []
    for k, is_prime in enumerate(sieve):
        if is_prime:
            res.append(k)

    return res


def valuation(n, p):
    """Returns the p-adic valuation of n."""
    res = 0
    while n % p == 0:
        n //= p
        res += 1

    return res


def count_divisors(n):
    """Returns the number of divisors of n."""
    count = 1
    for p in primes(n):
        count *= valuation(n, p) + 1

    return count


def get_total_x(a, b):
    m = 1
    for value in a:
        m = m * value // gcd(m, value)

    g = 0
    for value in b:
        g = gcd(g, value)

    if g % m:
        return 0
    else:
        return count_divisors(g // m)


if __name__ == '__main__':
    print(get_total_x([2, 4], [16, 32, 96]))  # 3
