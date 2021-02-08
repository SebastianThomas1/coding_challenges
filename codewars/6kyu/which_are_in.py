# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/550554fd08b86f84fe000a58
#
# Which are in?

import bisect


def in_array(array1, array2):
    result = []
    for word1 in array1:
        for word2 in array2:
            if word1 in word2 and word1 not in result:
                bisect.insort(result, word1)
    return result


if __name__ == '__main__':
    print(in_array(['live', 'arp', 'strong'],
                   ['lively', 'alive', 'harp', 'sharp', 'armstrong']))
    # ['arp', 'live', 'strong']
    print(in_array(['arp', 'mice', 'bull'],
                   ['lively', 'alive', 'harp', 'sharp', 'armstrong']))
    # ['arp']
