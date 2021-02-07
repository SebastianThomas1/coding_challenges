# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/cats-and-a-mouse
#
# Cats and a Mouse

def cat_and_mouse(x, y, z):
    diff_a = abs(x - z)
    diff_b = abs(y - z)
    if diff_a < diff_b:
        return 'Cat A'
    elif diff_a > diff_b:
        return 'Cat B'
    else:
        return 'Mouse C'


if __name__ == '__main__':
    print(cat_and_mouse(2, 5, 4))  # Cat B
    print(cat_and_mouse(1, 2, 3))  # Cat B
    print(cat_and_mouse(1, 3, 2))  # Mouse C
