# Sebastian Thomas (coding at sebastianthomas dot de)

# https://app.codility.com/programmers/lessons/7-stacks_and_queues/nesting/
#
# Nesting
#
# Determine whether a given string of parentheses (single type) is
# properly nested.
#
# A string S consisting of N characters is called properly nested if:
#   - S is empty;
#   - S has the form "(U)" where U is a properly nested string;
#   - S has the form "VW" where V and W are properly nested strings.
# For example, string "(()(())())" is properly nested but string "())"
# isn't.
#
# Write a function:
#   def solution(S)
# that, given a string S consisting of N characters, returns 1 if string
# S is properly nested and 0 otherwise.
#
# For example, given S = "(()(())())", the function should return 1 and
# given S = "())", the function should return 0, as explained above.
#
# Write an efficient algorithm for the following assumptions:
#   - N is an integer within the range [0..1,000,000];
#   - string S consists only of the characters "(" and/or ")".

def solution(s):
    opened_parentheses = 0
    for char in s:
        if char == '(':
            opened_parentheses += 1
        else:
            if not opened_parentheses:
                return 0
            opened_parentheses -= 1

    return 1 - int(bool(opened_parentheses))


if __name__ == '__main__':
    print(solution('(()(())())'))  # 1
    print(solution('())'))  # 0
    print(solution('('))  # 0
