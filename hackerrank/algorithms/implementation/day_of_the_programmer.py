# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/day-of-the-programmer
#
# Day of the Programmer

def day_of_programmer(year):
    if year > 1918:
        return '{}.09.{}'.format(13 if (year % 4 or year % 400
                                        and year % 100 == 0)
                                 else 12, year)
    elif year < 1918:
        return '{}.09.{}'.format(13 if year % 4 else 12, year)
    else:
        return '26.09.1918'


if __name__ == '__main__':
    print(day_of_programmer(2017))  # 13.09.2017
    print(day_of_programmer(2016))  # 12.09.2016
    print(day_of_programmer(1800))  # 12.09.1800
