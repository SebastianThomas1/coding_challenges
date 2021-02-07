# 70. Climbing Stairs
#
# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways
# can you climb to the top?

def climb_stairs(n: int) -> int:
    if n == 0 or n == 1:
        return 1

    last_count = 1
    count = 1
    for _ in range(n - 1):
        last_count, count = count, last_count + count

    return count


if __name__ == '__main__':
    print(climb_stairs(2))  # 2
    print(climb_stairs(3))  # 3
