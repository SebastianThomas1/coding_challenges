# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/5ce399e0047a45001c853c2b
#
# Sums of Parts

def parts_sums(ls):
    sums = [sum(ls)]
    for idx in range(len(ls)):
        sums.append(sums[-1] - ls[idx])
    return sums


if __name__ == '__main__':
    print(parts_sums([]))  # [0]
    print(parts_sums([0, 1, 3, 6, 10]))  # [20, 20, 19, 16, 10, 0]
    print(parts_sums([1, 2, 3, 4, 5, 6]))  # [21, 20, 18, 15, 11, 6, 0]
    print(parts_sums([744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810,
                      2579358]))
    # [10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414,
    #  9291270, 2581057, 2580168, 2579358, 0]
