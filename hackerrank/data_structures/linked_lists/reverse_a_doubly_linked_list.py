# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list
#
# Reverse a doubly linked list

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


def reverse(head):
    if head is None:
        return None

    while True:
        head.prev, head.next = head.next, head.prev
        if head.prev:
            head = head.prev
        else:
            return head
