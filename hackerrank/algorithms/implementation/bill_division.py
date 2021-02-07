# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/bon-appetit
#
# Bill Division

def bon_appetit(bill, k, b):
    cost = (sum(bill) - bill[k]) / 2
    if cost == b:
        print('Bon Appetit')
    else:
        print(int(b - cost))


if __name__ == '__main__':
    bon_appetit([3, 10, 2, 9], 1, 12)  # 5
    bon_appetit([3, 10, 2, 9], 1, 7)  # Bon Appetit
