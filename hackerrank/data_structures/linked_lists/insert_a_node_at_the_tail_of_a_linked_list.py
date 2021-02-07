# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list
#
# Insert a Node at the Tail of a Linked List

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


def insert_node_at_tail(head, data):
    if head is None:
        return SinglyLinkedListNode(data)

    current_node = head
    while current_node.next:
        current_node = current_node.next

    current_node.next = SinglyLinkedListNode(data)

    return head
