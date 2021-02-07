# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/reverse-a-linked-list
#
# Reverse a linked list

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


def reverse(head):
    current_node = head
    predecessor = None
    while current_node:
        successor = current_node.next
        current_node.next = predecessor
        predecessor = current_node
        current_node = successor

    return predecessor
