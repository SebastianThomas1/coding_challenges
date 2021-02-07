# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list
#
# Insert a node at a specific position in a linked list

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


def insert_node_at_position(head, data, position):
    if position == 0:
        new_node = SinglyLinkedListNode(data)
        new_node.next = head

        return new_node
    else:
        current_node = head
        while position != 1:
            current_node = current_node.next
            position -= 1

        successor = current_node.next
        current_node.next = SinglyLinkedListNode(data)
        current_node.next.next = successor

        return head
