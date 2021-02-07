# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/largest-rectangle
#
# Largest Rectangle

def largest_rectangle(h):
    h.append(0)

    stack = []
    area = 0

    for idx in range(len(h)):
        while stack and h[stack[-1]] > h[idx]:
            height_idx = stack.pop()
            start_idx = stack[-1] + 1 if stack else 0
            area = max(area, h[height_idx] * (idx - start_idx))

        stack.append(idx)

    return area


if __name__ == '__main__':
    print(largest_rectangle([3, 2, 3]))  # 6
    print(largest_rectangle([1, 2, 3, 4, 5]))  # 9
    print(largest_rectangle([1, 3, 5, 9, 11]))  # 18
    print(largest_rectangle([11, 11, 10, 10, 10]))  # 50
    print(largest_rectangle([3, 2, 5, 6, 1, 4, 4]))  # 10
    print(largest_rectangle([3, 1, 5, 6, 2, 4, 4]))  # 10
