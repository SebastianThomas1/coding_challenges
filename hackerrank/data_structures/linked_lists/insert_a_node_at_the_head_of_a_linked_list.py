# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list
#
# Insert a node at the head of a linked list

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


def insert_node_at_head(head, data):
    new_head = SinglyLinkedListNode(data)
    new_head.next = head

    return new_head
