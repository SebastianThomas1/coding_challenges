# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle
#
# Cycle Detection

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


def has_cycle(head):
    fast_node = head
    slow_node = head
    while fast_node and fast_node.next:
        fast_node = fast_node.next.next
        slow_node = slow_node.next

        if fast_node is slow_node:
            return 1

    return 0
