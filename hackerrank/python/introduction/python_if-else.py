# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/py-if-else
#
# Python If-Else

def if_else(n):
    if n % 2 == 1 or 6 <= n <= 20:
        print('Weird')
    elif 2 <= n <= 6 or n > 21:
        print('Not Weird')


if __name__ == '__main__':
    if_else(3)  # Weird
    if_else(24)  # Not Weird
