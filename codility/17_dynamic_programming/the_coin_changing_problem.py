# Sebastian Thomas (coding at sebastianthomas dot de)

# https://codility.com/media/train/15-DynamicProgramming.pdf
#
# The Coin Changing Problem

def dynamic_coin_changing(coins, k):
    n = len(coins)

    min_counts = [0] + [float('inf')] * k
    for i in range(1, n + 1):
        for j in range(coins[i - 1], k + 1):
            min_counts[j] = min(min_counts[j],
                                min_counts[j - coins[i - 1]] + 1)

    return min_counts


if __name__ == '__main__':
    print(dynamic_coin_changing([1, 3, 4], 6))  # [0, 1, 2, 1, 1, 2, 2]
