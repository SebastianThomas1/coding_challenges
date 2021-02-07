# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/ctci-ransom-note
#
# Hash Tables: Ransom Note

from collections import Counter


def checkMagazine(magazine, note):
    counter_magazine = Counter(magazine)
    counter_note = Counter(note)

    for word in counter_note:
        if counter_note[word] > counter_magazine[word]:
            print('No')
            return

    print('Yes')


if __name__ == '__main__':
    checkMagazine('give me one grand today night',
                  'give one grand today')  # Yes
    checkMagazine('two times three is not four',
                  'two times two is four')  # No
    checkMagazine('ive got a lovely bunch of coconuts',
                  'ive got some coconuts')  # No
