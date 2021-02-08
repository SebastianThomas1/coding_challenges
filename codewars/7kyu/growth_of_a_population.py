# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/563b662a59afc2b5120000c6
#
# Growth of a Population

def nb_year(p0, percent, aug, p):
    percent = percent / 100
    n = 0
    population = p0

    while population < p:
        population += population * percent + aug
        n += 1

    return n


if __name__ == '__main__':
    print(nb_year(1500, 5, 100, 5000))  # 15
    print(nb_year(1500000, 2.5, 10000, 2000000))  # 10
    print(nb_year(1500000, 0.25, 1000, 2000000))  # 94
