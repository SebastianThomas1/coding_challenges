# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list
#
# Inserting a Node Into a Sorted Doubly Linked List

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


def sorted_insert(head, data):
    if head is None:
        return DoublyLinkedListNode(data)

    if data <= head.data:
        head.prev = DoublyLinkedListNode(data)
        head.prev.next = head
        return head.prev

    current_node = head
    while current_node.next and current_node.next.data < data:
        current_node = current_node.next

    if current_node.next is None:
        current_node.next = DoublyLinkedListNode(data)
        current_node.next.prev = current_node
    else:
        successor = current_node.next
        current_node.next = DoublyLinkedListNode(data)
        current_node.next.prev = current_node
        current_node.next.next = successor
        successor.prev = current_node.next

    return head
