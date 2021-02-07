# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/maximum-element
#
# Maximum Element

def maximum_element(queries):
    stack = []

    for query in queries:
        query = query.split()
        if int(query[0]) == 1:
            stack.append(
                max(stack[-1] if stack else int(query[1]), int(query[1])))
        elif int(query[0]) == 2:
            stack.pop()
        else:
            print(stack[-1])


if __name__ == '__main__':
    maximum_element(['1 97', '2', '1 20', '2', '1 26', '1 20', '2', '3',
                     '1 91', '3'])
