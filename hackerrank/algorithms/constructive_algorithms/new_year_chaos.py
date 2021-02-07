# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/new-year-chaos
#
# New Year Chaos

def minimum_bribes(q):
    count = 0
    for i in range(len(q) - 1, 1, -1):
        if q[i] != i + 1:
            try:
                idx = q.index(i + 1, i - 2, i)
            except ValueError:
                print('Too chaotic')
                return
            else:
                if idx == i - 2:
                    q[i - 2], q[i - 1] = q[i - 1], q[i - 2]
                    count += 1
                q[i - 1], q[i] = q[i], q[i - 1]
                count += 1

    if q[1] != 2:
        q[0], q[1] = q[1], q[0]
        count += 1

    print(count)


if __name__ == '__main__':
    minimum_bribes([2, 1, 5, 3, 4])  # 3
    minimum_bribes([2, 5, 1, 3, 4])  # Too chaotic
    minimum_bribes([5, 1, 2, 3, 7, 8, 6, 4])  # Too chaotic
    minimum_bribes([1, 2, 5, 3, 7, 8, 6, 4])  # 7
