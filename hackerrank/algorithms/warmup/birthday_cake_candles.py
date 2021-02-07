# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/birthday-cake-candles
#
# Birthday Cake Candles

def birthday_cake_candles(candles):
    max_value = None
    count = 0
    for value in candles:
        if max_value is None or value > max_value:
            max_value = value
            count = 1
        elif max_value and value == max_value:
            count += 1

    return count


if __name__ == '__main__':
    print(birthday_cake_candles([3, 2, 1, 3]))  # 2
    print(birthday_cake_candles([2, 3, 1, 3]))  # 2
