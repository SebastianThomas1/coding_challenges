# Sebastian Thomas (coding at sebastianthomas dot de)

# https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/
#
# Brackets
#
# Determine whether a given string of parentheses (multiple types) is
# properly nested.
#
# A string S consisting of N characters is considered to be properly
# nested if any of the following conditions is true:
#   - S is empty;
#   - S has the form "(U)" or "[U]" or "{U}" where U is a properly
#     nested string;
#   - S has the form "VW" where V and W are properly nested strings.
#
# For example, the string "{[()()]}" is properly nested but "([)()]" is
# not.
#
# Write a function:
#   def solution(S)
# that, given a string S consisting of N characters, returns 1 if S is
# properly nested and 0 otherwise.
#
# For example, given S = "{[()()]}", the function should return 1 and
# given S = "([)()]", the function should return 0, as explained above.
#
# Write an efficient algorithm for the following assumptions:
#   - N is an integer within the range [0..200,000];
#   - string S consists only of the following characters: "(", "{", "[",
#     "]", "}" and/or ")".

OPEN_PARENTHESES = {')': '(', ']': '[', '}': '{'}


def solution(s):
    opened_parentheses = []
    for char in s:
        if char in '([{':
            opened_parentheses.append(char)
        elif char in ')]}':
            if (not opened_parentheses
                    or opened_parentheses.pop() != OPEN_PARENTHESES[char]):
                return 0

    return int(not opened_parentheses)


if __name__ == '__main__':
    print(solution('{[()()]}'))  # 1
    print(solution('([)()]'))  # 0
    print(solution(')'))  # 0
