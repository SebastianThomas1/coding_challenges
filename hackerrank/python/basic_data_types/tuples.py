# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/python-tuples
#
# Tuples

def print_hash_as_tuple(integer_list):
    print(hash(tuple(integer_list)))


if __name__ == '__main__':
    print_hash_as_tuple([1, 2])  # -3550055125485641917
