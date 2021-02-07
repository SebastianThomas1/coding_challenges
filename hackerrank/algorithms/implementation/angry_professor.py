# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/angry-professor
#
# Angry Professor

def angry_professor(k, a):
    return 'NO' if sum(1 for value in a if value <= 0) >= k else 'YES'


if __name__ == '__main__':
    print(angry_professor(3, [-1, -3, 4, 2]))  # 'YES'
    print(angry_professor(2, [0, -1, 2, 1]))  # 'NO'
