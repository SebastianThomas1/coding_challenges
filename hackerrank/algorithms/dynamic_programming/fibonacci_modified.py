# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/fibonacci-modified
#
# Fibonacci Modified

def fibonacci_modified(t1, t2, n):
    if n == 1:
        return t1
    if n == 2:
        return t2

    for idx in range(3, n + 1):
        t1, t2 = t2, t1 + t2*t2

    return t2


if __name__ == '__main__':
    print(fibonacci_modified(0, 1, 5))  # 5
    print(fibonacci_modified(0, 1, 6))  # 27
