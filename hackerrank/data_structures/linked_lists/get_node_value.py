# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail
#
# Get Node Value

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


def get_node(head, position_from_tail):
    # determine length
    length = 0
    current_node = head
    while current_node:
        length += 1
        current_node = current_node.next

    remaining_steps = length - position_from_tail - 1
    while remaining_steps != 0:
        head = head.next
        remaining_steps -= 1

    return head.data
