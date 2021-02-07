# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/staircase
#
# Staircase

def staircase(n):
    for idx in range(1, n + 1):
        print(' ' * (n - idx) + '#' * idx)


if __name__ == '__main__':
    staircase(6)
    #      #
    #     ##
    #    ###
    #   ####
    #  #####
    # ######
