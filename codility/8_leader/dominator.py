# Sebastian Thomas (coding at sebastianthomas dot de)

# https://app.codility.com/programmers/lessons/8-leader/dominator/
#
# Dominator
#
# Find an index of an array such that its value occurs at more than half
# of indices in the array.
#
# An array A consisting of N integers is given. The dominator of array A
# is the value that occurs in more than half of the elements of A.
#
# For example, consider array A such that
#   A[0] = 3    A[1] = 4    A[2] =  3
#   A[3] = 2    A[4] = 3    A[5] = -1
#   A[6] = 3    A[7] = 3
# The dominator of A is 3 because it occurs in 5 out of 8 elements of A
# (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a
# half of 8.
#
# Write a function
#   def solution(A)
# that, given an array A consisting of N integers, returns index of any
# element of array A in which the dominator of A occurs. The function
# should return −1 if array A does not have a dominator.
#
# For example, given array A such that
#   A[0] = 3    A[1] = 4    A[2] =  3
#   A[3] = 2    A[4] = 3    A[5] = -1
#   A[6] = 3    A[7] = 3
# the function may return 0, 2, 4, 6 or 7, as explained above.
#
# Write an efficient algorithm for the following assumptions:
#   - N is an integer within the range [0..100,000];
#   - each element of array A is an integer within the range
#     [−2,147,483,648..2,147,483,647].

def solution(a):
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

    idx_leader = -1
    if size:  # stack is not empty: count occurrences of stack_value
        n = len(a)
        count = 0
        idx_candidate = -1
        for idx in range(n):
            if a[idx] == stack_value:
                if not count:  # save first occurrence of stack_value
                    idx_candidate = idx
                count += 1
        if count > n // 2:
            # if count is higher than half of length of a, then
            # stack_value is a leader
            idx_leader = idx_candidate

    return idx_leader


if __name__ == '__main__':
    print(solution([3, 4, 3, 2, 3, -1, 3, 3]))  # 0 (or 2, 4, 6, 7)
    print(solution([4, 3, 2, 3, -1, 3, 3]))  # 1 (or 3, 5, 6)
    print(solution([4, 3, 2, -1, 3, 3]))  # -1
