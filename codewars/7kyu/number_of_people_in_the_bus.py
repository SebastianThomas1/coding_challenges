# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/5648b12ce68d9daa6b000099
#
# Number of people in the bus

def number(bus_stops):
    return sum(into - off for into, off in bus_stops)


if __name__ == '__main__':
    print(number([[10, 0], [3, 5], [5, 8]]))  # 5
    print(number([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]]))
    # 17
    print(number([[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]]))
    # 21
