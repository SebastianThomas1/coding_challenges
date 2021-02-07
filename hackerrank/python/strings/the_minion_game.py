# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/the-minion-game
#
# The Minion Game

def minion_game(string):
    length = len(string)

    score1 = 0
    score2 = 0
    for idx, char in enumerate(string):
        if char not in 'AEIOU':
            score1 += length - idx
        else:
            score2 += length - idx

    if score1 > score2:
        print('Stuart {}'.format(score1))
    elif score2 > score1:
        print('Kevin {}'.format(score2))
    else:
        print('Draw')


if __name__ == '__main__':
    minion_game('BANANA')  # Stuart 12
