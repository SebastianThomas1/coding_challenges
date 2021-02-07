# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/counting-valleys
#
# Counting Valleys

def counting_valleys(path):
    count = 0
    level = 0
    for step in path:
        if level == 0 and step == 'D':
            count += 1

        level += 1 if step == 'U' else -1

    return count


if __name__ == '__main__':
    print(counting_valleys('UDDDUDUU'))  # 1
