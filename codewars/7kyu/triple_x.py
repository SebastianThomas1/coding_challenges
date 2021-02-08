# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/568dc69683322417eb00002c
#
# L2: Triple X

def triple_x(s):
    if len(s) < 3:
        return False
    for idx, c in enumerate(s[:-2]):
        if c == 'x':
            return s[idx + 1] == 'x' and s[idx + 2] == 'x'
    return False


if __name__ == '__main__':
    print(triple_x('abraxxxas'))  # True
    print(triple_x('xoxotrololololololoxxx'))  # False
    print(triple_x('softX kitty, warm kitty, xxxxx'))  # True
    print(triple_x('softx kitty, warm kitty, xxxxx'))  # False
