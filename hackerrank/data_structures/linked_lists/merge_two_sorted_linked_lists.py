# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists
#
# Merge two sorted linked lists

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


def merge_lists(head1, head2):
    if head1 is None and head2 is None:
        return None

    if head1 and head2 and head1.data <= head2.data or head2 is None:
        head = head1
        tail = head1
        head1 = head1.next
    else:
        head = head2
        tail = head2
        head2 = head2.next

    while head1 or head2:
        if head1 and head2 and head1.data <= head2.data or head2 is None:
            tail.next = head1
            tail = tail.next
            head1 = head1.next
        else:
            tail.next = head2
            tail = tail.next
            head2 = head2.next

    return head
