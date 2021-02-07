# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/nested-list
#
# Nested Lists

def students_with_second_lowest_grade(students):
    min_score = None
    students_with_min_score = []
    second_min_score = None
    students_with_second_min_score = []

    for name, score in students:
        if min_score is None or min_score > score:
            second_min_score = min_score
            students_with_second_min_score = students_with_min_score
            min_score = score
            students_with_min_score = [name]
        elif min_score == score:
            students_with_min_score.append(name)
        elif (score > min_score
              and (second_min_score is None or second_min_score > score)):
            second_min_score = score
            students_with_second_min_score = [name]
        elif second_min_score == score:
            students_with_second_min_score.append(name)

    return sorted(students_with_second_min_score)


if __name__ == '__main__':
    print(students_with_second_lowest_grade(
        [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41],
         ['Harsh', 39]]))  # ['Berry', 'Harry']
