# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/522551eee9abb932420004a0
#
# N-th Fibonacci

def nth_fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return nth_fib(n - 2) + nth_fib(n - 1)


if __name__ == '__main__':
    print(nth_fib(1))  # 0
    print(nth_fib(2))  # 1
    print(nth_fib(3))  # 1
    print(nth_fib(4))  # 2
    print(nth_fib(5))  # 3
    print(nth_fib(6))  # 5
    print(nth_fib(7))  # 8
