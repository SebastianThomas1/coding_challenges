# Sebastian Thomas (coding at sebastianthomas dot de)

# https://codility.com/media/train/15-DynamicProgramming.pdf
#
# Frog jumps

def frog(s, k, q):
    n = len(s)
    counts = [1] + [0] * k
    for j in range(1, k + 1):
        for i in range(n):
            if s[i] <= j:
                counts[j] += counts[j - s[i]]
                counts[j] %= q
    return counts[k]


if __name__ == '__main__':
    pass
