# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list
#
# Print the Elements of a Linked List

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


def print_linked_list(head):
    while head is not None:
        print(head.data)
        head = head.next
