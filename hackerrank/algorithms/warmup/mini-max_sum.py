# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/mini-max-sum
#
# Mini-Max Sum

def mini_max_sum(arr):
    total_sum = sum(arr)
    print('{} {}'.format(total_sum - max(arr), total_sum - min(arr)))


if __name__ == '__main__':
    mini_max_sum([1, 2, 3, 4, 5])  # 10 14
