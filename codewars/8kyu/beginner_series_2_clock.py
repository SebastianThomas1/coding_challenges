# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a
#
# Beginner Series #2 Clock

def past(h, m, s):
    return ((h*60 + m)*60 + s) * 1000


if __name__ == '__main__':
    print(past(0, 1, 1))  # 61000
    print(past(1, 1, 1))  # 3661000
    print(past(0, 0, 0))  # 0
    print(past(1, 0, 1))  # 3601000
    print(past(1, 0, 0))  # 3600000
