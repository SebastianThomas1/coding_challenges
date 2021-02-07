# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/strange-advertising
#
# Viral Advertising

def viral_advertising(n):
    def likes_generator(start):
        likes = start // 2
        while True:
            yield likes
            likes *= 3
            likes //= 2

    likes_sequence = likes_generator(5)

    return sum(next(likes_sequence) for _ in range(n))


if __name__ == '__main__':
    print(viral_advertising(3))  # 9
    print(viral_advertising(5))  # 24
