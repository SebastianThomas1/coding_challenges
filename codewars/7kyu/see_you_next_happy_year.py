# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/5ae7e3f068e6445bc8000046
#
# See You Next Happy Year

def next_happy_year(year):
    year += 1
    while len(set(str(year))) < 4:
        year += 1

    return year


if __name__ == '__main__':
    print(next_happy_year(7712))  # 7801
    print(next_happy_year(8989))  # 9012
    print(next_happy_year(1001))  # 1023
