# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/python-mutations
#
# Mutations

def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]


if __name__ == '__main__':
    print(mutate_string('abracadabra', 5, 'k'))
