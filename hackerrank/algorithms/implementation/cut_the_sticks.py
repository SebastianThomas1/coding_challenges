# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/cut-the-sticks
#
# Cut the sticks

def cut_the_sticks(arr):
    n_sticks = []
    arr = sorted(arr, reverse=True)
    while arr:
        n_sticks.append(len(arr))
        # determine length of shortest stick
        min_value = arr[-1]
        # cut lengths
        arr = [value - min_value for value in arr]
        # discard shortest sticks
        while arr and arr[-1] == 0:
            del arr[-1]

    return n_sticks


if __name__ == '__main__':
    print(cut_the_sticks([5, 4, 4, 2, 2, 8]))  # [6, 4, 2, 1]
    print(cut_the_sticks([1, 2, 3, 4, 3, 3, 2, 1]))  # [8, 6, 4, 1]
