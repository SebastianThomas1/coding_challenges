# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/write-a-function
#
# Write a function

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False


if __name__ == '__main__':
    print(is_leap(1990))  # False
