# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/balanced-brackets
#
# Balanced Brackets

OPEN_BRACKET = {')': '(', ']': '[', '}': '{'}


def is_balanced(s):
    stack = []
    for c in s:
        if c not in OPEN_BRACKET:  # opening bracket
            stack.append(c)
        elif stack and OPEN_BRACKET[c] == stack[-1]:
            # closing bracket, matching
            stack.pop()
        else:  # closing bracket, not matching
            return 'NO'

    return 'NO' if stack else 'YES'


if __name__ == '__main__':
    print(is_balanced('{[()]}'))  # YES
    print(is_balanced('{[(])}'))  # NO
    print(is_balanced('{{[[(())]]}}'))  # YES
