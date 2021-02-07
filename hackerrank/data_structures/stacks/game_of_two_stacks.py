# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/game-of-two-stacks
#
# Game of Two Stacks

def two_stacks(x, a, b):
    a.reverse()
    b.reverse()

    stack = []
    score = 0

    # remove as much values from a as possible
    while a:
        value = a.pop()
        reduced = x - value
        if reduced < 0:
            break
        else:
            x = reduced
            score += 1
            stack.append(value)

    max_score = score

    # virtually add values from b to the stack, and really
    # pop those values from a that oversizes the credit x
    # in between persist the maximal score
    while b:
        x -= b.pop()
        score += 1
        while stack and x < 0:
            x += stack.pop()
            score -= 1
        if x >= 0 and score > max_score:
            max_score = score

    return max_score


if __name__ == '__main__':
    print(two_stacks(10, [4, 2, 4, 6, 1], [2, 1, 8, 5]))  # 4
