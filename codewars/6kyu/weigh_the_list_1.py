# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/5fad2310ff1ef6003291a951
#
# Weigh The List #1

def weigh_the_list(a):
    b = [- a[0]*entry for entry in a]
    for entry in a:
        b[0] += entry*entry
    return b


if __name__ == '__main__':
    print(weigh_the_list([1, 2, 3, 4, 5, 6]))
    # e.g [-10, -1, -1, 1, 1, 1] or [90, -2, -3, -4, -5, -6]
    print(weigh_the_list([-13, 52]))  # e.g [4, 1] or [2704, 676]
    print(weigh_the_list([-1, 1]))  # e.g [1, 1]
    print(weigh_the_list([2, 2, 2, 2]))  # e.g [12, -4, -4, -4]
    print(weigh_the_list([2, 7, 3, 11, 5, 23, 47, 3]))
    # e.g [2951, -14, -6, -22, -10, -46, -94, -6]
    print(weigh_the_list([-1, 100, -100, 1]))  # e.g [20001, 100, -100, 1]
    print(weigh_the_list([1, 1, 1, -2]))  # e.g [6, -1, -1, 2]
    print(weigh_the_list([-2, 1, 1, 1]))  # e.g [3, 2, 2, 2]
