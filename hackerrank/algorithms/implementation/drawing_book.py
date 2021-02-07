# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/drawing-book
#
# Drawing Book

def page_count(n, p):
    return min(p // 2, n // 2 - p // 2)


if __name__ == '__main__':
    print(page_count(5, 3))  # 1
    print(page_count(6, 2))  # 1
    print(page_count(5, 4))  # 0
