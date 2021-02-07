# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/frequency-queries
#
# Frequency Queries

from collections import defaultdict


def freq_query(queries):
    counter = defaultdict(int)
    frequency_counter = defaultdict(int)
    output = []
    for operation, data in queries:
        if operation == 1:
            frequency_counter[counter[data]] \
                = max(0, frequency_counter[counter[data]] - 1)
            counter[data] += 1
            frequency_counter[counter[data]] += 1
        elif operation == 2:
            if counter[data] > 0:
                frequency_counter[counter[data]] \
                    = max(0, frequency_counter[counter[data]] - 1)
                counter[data] -= 1
                frequency_counter[counter[data]] += 1
        else:
            output.append(int(frequency_counter[data] > 0))

    return output


if __name__ == '__main__':
    print(freq_query([[1, 5], [1, 6], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5],
                      [3, 2]]))  # [0, 1]
    print(freq_query([[3, 4], [2, 1003], [1, 16], [3, 1]]))  # [0, 1]
    print(freq_query([[1, 3], [2, 3], [3, 2], [1, 4], [1, 5], [1, 5], [1, 4],
                      [3, 2], [2, 4], [3, 2]]))  # [0, 1, 1]
