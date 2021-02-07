# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse
#
# Print in Reverse

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


def reverse_print(head):
    head = reverse(head)

    current_node = head
    while current_node is not None:
        print(current_node.data)
        current_node = current_node.next

    reverse(head)
