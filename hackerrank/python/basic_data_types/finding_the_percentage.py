# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/finding-the-percentage
#
# Finding the percentage

def average_score(scores, query):
    scores_of_student = scores[query]
    return sum(scores_of_student) / len(scores_of_student)


if __name__ == '__main__':
    print('{:.2f}'.format(average_score({'Krishna': [67, 68, 69],
                                         'Arjun': [70, 98, 63],
                                         'Malika': [52, 56, 60]},
                                        'Malika')))  # 56.00
    print('{:.2f}'.format(average_score({'Harsh': [25, 26.5, 28],
                                         'Anurag': [26, 28, 30]},
                                        'Harsh')))  # 26.50
