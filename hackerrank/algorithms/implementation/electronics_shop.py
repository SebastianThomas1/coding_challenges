# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/electronics-shop
#
# Electronics Shop

def get_money_spent(keyboards, drives, b):
    costs = {keyboard + drive for keyboard in keyboards for drive in drives
             if keyboard + drive <= b}
    return max(costs) if costs else -1


if __name__ == '__main__':
    print(get_money_spent([3, 1], [5, 2, 8], 10))  # 9
    print(get_money_spent([4], [5], 5))  # -1
