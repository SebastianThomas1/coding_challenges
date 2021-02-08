# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/5277c8a221e209d3f6000b56
#
# Valid Braces

def valid_braces(string):
    while '()' in string or '[]' in string or '{}' in string:
        string = string.replace('()', '').replace('[]', '').replace('{}', '')

    return string == ''


if __name__ == '__main__':
    print(valid_braces('()'))  # True
    print(valid_braces('[(])'))  # False
