# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/5656b6906de340bd1b0000ac
#
# Two to One

def longest(s1, s2):
    return ''.join(sorted(set(s1 + s2)))


if __name__ == '__main__':
    print(longest('aretheyhere', 'yestheyarehere'))  # aehrsty
    print(longest('loopingisfunbutdangerous', 'lessdangerousthancoding'))
    # abcdefghilnoprstu
    print(longest('inmanylanguages', 'theresapairoffunctions'))
    # acefghilmnoprstuy
