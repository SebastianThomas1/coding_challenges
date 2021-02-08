# Sebastian Thomas (coding at sebastianthomas dot de)

# https://app.codility.com/programmers/lessons/8-leader/equi_leader/
#
# equi_leader
#
# Find the index S such that the leaders of the sequences
# A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N - 1] are the
# same.
#
# A non-empty array A consisting of N integers is given.
#
# The leader of this array is the value that occurs in more than half of
# the elements of A.
#
# An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences
# A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have
# leaders of the same value.
#
# For example, given array A such that:
#   A[0] = 4
#   A[1] = 3
#   A[2] = 4
#   A[3] = 4
#   A[4] = 4
#   A[5] = 2
# we can find two equi leaders:
#   - 0, because sequences: (4) and (3, 4, 4, 4, 2) have the same
#     leader, whose value is 4.
#   - 2, because sequences: (4, 3, 4) and (4, 4, 2) have the same
#     leader, whose value is 4.
# The goal is to count the number of equi leaders.
#
# Write a function:
#   def solution(A)
# that, given a non-empty array A consisting of N integers, returns the
# number of equi leaders.
#
# For example, given:
#   A[0] = 4
#   A[1] = 3
#   A[2] = 4
#   A[3] = 4
#   A[4] = 4
#   A[5] = 2
# the function should return 2, as explained above.
#
# Write an efficient algorithm for the following assumptions:
#   - N is an integer within the range [1..100,000];
#   - each element of array A is an integer within the range
#     [−1,000,000,000..1,000,000,000].

def indices_of_leader(a):
    if not a:
        return -1

    # build stack to remove different entries
    stack_value = None
    size = 0
    for entry in a:
        if size:  # we have already a value on the stack
            if stack_value != entry:
                size -= 1  # remove entry and value from stack
            else:
                size += 1  # add entry to stack
        else:  # stack is empty
            stack_value = entry
            size += 1

    idces_leader = []
    if size:  # stack is not empty: count occurrences of stack_value
        n = len(a)
        idces_candidate = []
        for idx in range(n):
            if a[idx] == stack_value:
                idces_candidate.append(idx)
        if len(idces_candidate) > n // 2:
            idces_leader = idces_candidate

    return idces_leader


def prefix_counts_of_leader(a):
    n = len(a)
    idces_leader = indices_of_leader(a)
    p = [0] * (n + 1)
    for idx, idx_leader in enumerate(idces_leader):
        p[idx_leader + 1] = idx + 1

    current_prefix_count = 0
    for idx, entry in enumerate(p):
        if entry:
            current_prefix_count = entry
        else:
            p[idx] = current_prefix_count

    return p


def solution(a):
    n = len(a)
    pref = prefix_counts_of_leader(a)
    count_of_leader = pref[-1]

    count_equi_leader = 0
    for idx, prefix_count in enumerate(pref):
        if (prefix_count > idx // 2
                and count_of_leader - prefix_count > (n - idx) // 2):
            count_equi_leader += 1

    return count_equi_leader


if __name__ == '__main__':
    print(solution([4, 3, 4, 4, 4, 2]))  # 2
    print(solution([3, 4, 3, 2, 3, -1, 3, 3]))  # 4
    print(solution([3, 4, 2, 3, -1, 3, 3]))  # 0
