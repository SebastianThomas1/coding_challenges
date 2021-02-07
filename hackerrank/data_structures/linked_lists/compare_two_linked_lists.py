# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/compare-two-linked-lists
#
# Compare two linked lists

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


def compare_lists(head1, head2):
    while head1 and head2:
        if head1.data != head2.data:
            return 0
        head1 = head1.next
        head2 = head2.next

    return 1 if head1 is None and head2 is None else 0
