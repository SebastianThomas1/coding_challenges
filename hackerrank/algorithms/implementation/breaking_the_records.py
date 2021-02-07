# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/breaking-best-and-worst-records
#
# Breaking the Records

def breaking_records(scores):
    min_score = max_score = None

    count_min_breaking = count_max_breaking = 0
    for score in scores:
        if min_score and score < min_score:
            min_score = score
            count_min_breaking += 1
        elif max_score and score > max_score:
            max_score = score
            count_max_breaking += 1
        elif min_score is None and max_score is None:
            min_score = max_score = score

    return count_max_breaking, count_min_breaking


if __name__ == '__main__':
    print(breaking_records([10, 5, 20, 20, 4, 5, 2, 25, 1]))  # 2, 4
    print(breaking_records([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]))
    # 4, 0
