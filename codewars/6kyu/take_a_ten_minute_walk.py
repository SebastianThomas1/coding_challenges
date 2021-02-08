# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/54da539698b8a2ad76000228
#
# Take a Ten Minute Walk

def is_valid_walk(walk):
    return (len(walk) == 10 and walk.count('n') == walk.count('s')
            and walk.count('e') == walk.count('w'))


if __name__ == '__main__':
    print(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))
    # True
    print(is_valid_walk(['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w',
                         'e']))  # False
    print(is_valid_walk(['w']))  # False
    print(is_valid_walk(['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))
    # False
