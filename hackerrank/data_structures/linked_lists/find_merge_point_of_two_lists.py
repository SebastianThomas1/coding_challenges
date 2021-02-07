# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists
#
# Find Merge Point of Two Lists

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


def length(head):
    n = 0
    while head:
        n += 1
        head = head.next

    return n


def find_merge_node(head1, head2):
    length1 = length(head1)
    length2 = length(head2)

    if length1 >= length2:
        steps = length1 - length2
        while steps != 0:
            head1 = head1.next
            steps -= 1
    else:
        steps = length2 - length1
        while steps != 0:
            head2 = head2.next
            steps -= 1

    while head1:
        if head1 is head2:
            return head1.data
        else:
            head1 = head1.next
            head2 = head2.next
