# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/merge-the-tools
#
# Merge the Tools!

def remove_duplicates(string):
    chars = []
    unique_chars = set()
    for char in string:
        if char not in unique_chars:
            chars.append(char)
            unique_chars.add(char)
    return ''.join(chars)


def merge_the_tools(string, k):
    n_substrings = len(string) // k
    for idx in range(n_substrings):
        print(remove_duplicates(string[idx*k:(idx + 1)*k]))


if __name__ == '__main__':
    merge_the_tools('AABCAAADA', 3)
    # AB
    # CA
    # AD
