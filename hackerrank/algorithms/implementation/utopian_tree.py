# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/utopian-tree
#
# Utopian Tree

def utopian_tree(n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return utopian_tree(n - 1) + 1
    else:
        return 2*utopian_tree(n - 1)


if __name__ == '__main__':
    print(utopian_tree(5))  # 14
    print(utopian_tree(0))  # 1
    print(utopian_tree(1))  # 2
    print(utopian_tree(4))  # 7
