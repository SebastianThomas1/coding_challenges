# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/grading
#
# Grading Students

def round_grade(grade):
    if grade >= 38:
        remainder = grade % 5
        if remainder > 2:
            grade += (5 - remainder)
    return grade


def grading_students(grades):
    return [round_grade(grade) for grade in grades]


if __name__ == '__main__':
    print(grading_students([73, 67, 38, 33]))  # [75, 67, 40, 33]
