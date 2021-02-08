# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/5d68d05e7a60ba002b0053f6
#
# Bonuses

def bonus(arr, s):
    const = s / sum(1/a for a in arr)
    return [round(const / a) for a in arr]


if __name__ == '__main__':
    print(bonus([18, 15, 12], 851))  # [230, 276, 345]
    print(bonus([30, 27, 8, 14, 7], 34067))
    # [2772, 3080, 10395, 5940, 11880]
    print(bonus([22, 3, 15], 18228))  # [1860, 13640, 2728]
    print(bonus([8, 14, 11], 23541))  # [10241, 5852, 7448]
    print(bonus([8, 20, 17], 25281))  # [13515, 5406, 6360]
    print(bonus([25, 22, 15, 22, 22], 5213))
    # [858, 975, 1430, 975, 975]
    print(bonus([10, 11, 30, 12, 17, 23, 30, 11, 17, 10], 1788210))
    # [258060, 234600, 86020, 215050, 151800, 112200, 86020, 234600,
    #  151800, 258060]
