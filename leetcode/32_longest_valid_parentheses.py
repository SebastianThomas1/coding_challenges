# 32. Longest Valid Parentheses
#
# Given a string containing just the characters '(' and ')', find the
# length of the longest valid (well-formed) parentheses substring.


def longest_valid_parentheses(s: str) -> int:
    lengths = [0] * len(s)
    for idx in range(1, len(s)):
        if s[idx] == ')':
            if s[idx - 1] == '(':
                lengths[idx] = lengths[idx - 2] + 2 if idx > 1 else 2
            elif idx > lengths[idx - 1] \
                    and s[idx - lengths[idx - 1] - 1] == '(':
                lengths[idx] = (lengths[idx - lengths[idx - 1] - 2]
                                if idx > lengths[idx - 1] + 1 else 0) \
                               + lengths[idx - 1] + 2

    return max(lengths) if lengths else 0


if __name__ == '__main__':
    print(longest_valid_parentheses('(()'))  # 2
    print(longest_valid_parentheses(')()())'))  # 4
    print(longest_valid_parentheses(''))  # 0
    print(longest_valid_parentheses('()'))  # 2
    print(longest_valid_parentheses('(()))())('))  # 4
    print(longest_valid_parentheses(')(()())))()'))  # 6
    print(longest_valid_parentheses('((())(())'))  # 8
    print(longest_valid_parentheses('((())(()'))  # 4
