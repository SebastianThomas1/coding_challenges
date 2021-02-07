# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/string-validators
#
# String Validators

def string_validators(string):
    return (any(char.isalnum() for char in string),
            any(char.isalpha() for char in string),
            any(char.isdigit() for char in string),
            any(char.islower() for char in string),
            any(char.isupper() for char in string))


if __name__ == '__main__':
    for has_property in string_validators('qA2'):
        print(has_property)
