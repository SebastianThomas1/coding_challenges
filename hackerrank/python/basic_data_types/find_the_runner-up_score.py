# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list
#
# Find the Runner-Up Score!

def runner_up_score(scores):
    max_score = None
    second_max_score = None
    for score in scores:
        if max_score is None or max_score < score:
            second_max_score = max_score
            max_score = score
        elif (score < max_score
              and (second_max_score is None or second_max_score < score)):
            second_max_score = score

    return second_max_score


if __name__ == '__main__':
    print(runner_up_score([2, 3, 6, 6, 5]))  # 5
