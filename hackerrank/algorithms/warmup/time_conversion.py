# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/time-conversion
#
# Time Conversion

def time_conversion(s):
    if s[-2:] == 'PM' and s[:2] != '12':
        res = str(int(s[:2]) + 12) + s[2:-2]
    elif s[-2:] == 'AM' and s[:2] == '12':
        res = '00' + s[2:-2]
    else:
        res = s[:-2]

    return res


if __name__ == '__main__':
    print(time_conversion('07:05:45PM'))  # 19:05:45
