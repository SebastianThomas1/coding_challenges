# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/compare-the-triplets
#
# Compare the Triplets

def compare_triplets(a, b):
    a_score = 0
    b_score = 0
    for idx in range(3):
        if a[idx] > b[idx]:
            a_score += 1
        elif a[idx] < b[idx]:
            b_score += 1

    return a_score, b_score


if __name__ == '__main__':
    print(compare_triplets([5, 6, 7], [3, 6, 10]))  # 1, 1
    print(compare_triplets([17, 28, 30], [99, 16, 8]))  # 2, 1
