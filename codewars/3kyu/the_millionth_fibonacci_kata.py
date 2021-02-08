# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/53d40c1e2f13e331fc000c26
#
# The Millionth Fibonacci Kata

def fib(n):
    if n >= 0:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n % 2 == 0:
            c = fib(n/2)
            return (2*fib(n/2 - 1) + c)*c
        else:
            return fib((n + 1)/2 - 1)**2 + fib((n + 1)/2)**2
    else:
        if n % 2 == 0:
            return -fib(-n)
        else:
            return fib(-n)


if __name__ == '__main__':
    print(fib(0))  # 0
    print(fib(1))  # 1
    print(fib(2))  # 1
    print(fib(3))  # 2
    print(fib(4))  # 3
    print(fib(5))  # 5
    print(fib(1000))
    # 434665576869374564356885276750406258025646605173717804024817290895
    # 365554179490518904038798400792551692959225930803226347752096896232
    # 398733224711616429964409065331879382989696499285160037044761377951
    # 66849228875
